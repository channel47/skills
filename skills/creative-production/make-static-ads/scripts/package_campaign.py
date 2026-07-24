#!/usr/bin/env python3
"""Verify and package a finished static-ad campaign.

Expected layout:
  campaign/
    assets/c01-concept-name/c01-concept-name__4x5__1080x1350.png
    campaign.json  # optional metadata

The script validates filenames/dimensions, writes manifest.csv, creates review
sheets when ImageMagick is available, and writes a verified ZIP beside campaign.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


SPECS = {
    "4x5": (1080, 1350),
    "1x1": (1080, 1080),
    "9x16": (1080, 1920),
    "1.91x1": (1200, 628),
}
IMAGE_EXTS = {".png", ".jpg", ".jpeg"}
NAME_RE = re.compile(
    r"^(?P<concept>c\d{2}-[a-z0-9-]+)__"
    r"(?P<ratio>4x5|1x1|9x16|1\.91x1)__"
    r"(?P<width>\d+)x(?P<height>\d+)$"
)
MANIFEST_FIELDS = [
    "campaign_name",
    "test_variable",
    "concept_id",
    "concept_name",
    "strategic_angle",
    "audience",
    "headline",
    "cta",
    "ratio",
    "width",
    "height",
    "filename",
    "destination_url",
    "caveats",
]


def dimensions(path: Path) -> tuple[int, int]:
    """Read PNG/JPEG dimensions using only the Python standard library."""
    with path.open("rb") as handle:
        head = handle.read(24)
        if head.startswith(b"\x89PNG\r\n\x1a\n"):
            return struct.unpack(">II", head[16:24])
        if head[:2] != b"\xff\xd8":
            raise ValueError(f"Unsupported image format: {path}")
        handle.seek(2)
        while True:
            marker_start = handle.read(1)
            if not marker_start:
                break
            if marker_start != b"\xff":
                continue
            marker = handle.read(1)
            while marker == b"\xff":
                marker = handle.read(1)
            if marker in {b"\xd8", b"\xd9"}:
                continue
            length_bytes = handle.read(2)
            if len(length_bytes) != 2:
                break
            length = struct.unpack(">H", length_bytes)[0]
            if marker and marker[0] in {
                0xC0,
                0xC1,
                0xC2,
                0xC3,
                0xC5,
                0xC6,
                0xC7,
                0xC9,
                0xCA,
                0xCB,
                0xCD,
                0xCE,
                0xCF,
            }:
                data = handle.read(5)
                height, width = struct.unpack(">HH", data[1:5])
                return width, height
            handle.seek(length - 2, 1)
    raise ValueError(f"Could not read image dimensions: {path}")


def load_metadata(campaign: Path) -> dict:
    metadata_path = campaign / "campaign.json"
    if not metadata_path.exists():
        return {}
    with metadata_path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError("campaign.json must contain a JSON object")
    return value


def collect(campaign: Path, allow_missing: bool) -> list[dict]:
    assets = campaign / "assets"
    if not assets.is_dir():
        raise ValueError(f"Missing assets directory: {assets}")

    metadata = load_metadata(campaign)
    concepts_meta = metadata.get("concepts", {})
    if not isinstance(concepts_meta, dict):
        raise ValueError('campaign.json field "concepts" must contain a JSON object')
    for concept, concept_meta in concepts_meta.items():
        if not isinstance(concept_meta, dict):
            raise ValueError(
                f'campaign.json concept "{concept}" must contain a JSON object'
            )

    rows: list[dict] = []
    seen: dict[str, set[str]] = {}
    errors: list[str] = []

    files = sorted(
        path
        for path in assets.rglob("*")
        if path.is_file() and path.suffix.lower() in IMAGE_EXTS
    )
    if not files:
        raise ValueError(f"No PNG or JPEG assets found under {assets}")

    for path in files:
        match = NAME_RE.match(path.stem)
        if not match:
            errors.append(f"Invalid filename: {path.relative_to(campaign)}")
            continue
        info = match.groupdict()
        expected = SPECS[info["ratio"]]
        encoded = (int(info["width"]), int(info["height"]))
        actual = dimensions(path)
        if encoded != expected:
            errors.append(
                f"{path.name}: filename dimensions {encoded} do not match "
                f"required {expected}"
            )
        if actual != expected:
            errors.append(
                f"{path.name}: actual dimensions {actual} do not match "
                f"required {expected}"
            )

        concept = info["concept"]
        concept_ratios = seen.setdefault(concept, set())
        if info["ratio"] in concept_ratios:
            errors.append(f"{concept}: duplicate ratio {info['ratio']}")
        concept_ratios.add(info["ratio"])
        meta = concepts_meta.get(concept, {})
        rows.append(
            {
                "campaign_name": metadata.get("campaign_name", campaign.name),
                "test_variable": metadata.get("test_variable", ""),
                "concept_id": concept.split("-", 1)[0],
                "concept_name": meta.get("name", concept.split("-", 1)[1]),
                "strategic_angle": meta.get("strategic_angle", ""),
                "audience": meta.get("audience", ""),
                "headline": meta.get("headline", ""),
                "cta": meta.get("cta", ""),
                "ratio": info["ratio"],
                "width": actual[0],
                "height": actual[1],
                "filename": str(path.relative_to(campaign)),
                "destination_url": meta.get("destination_url", ""),
                "caveats": meta.get("caveats", ""),
            }
        )

    if not allow_missing:
        required = set(SPECS)
        for concept, ratios in seen.items():
            missing = sorted(required - ratios)
            if missing:
                errors.append(f"{concept}: missing ratios {', '.join(missing)}")

    if errors:
        raise ValueError("\n".join(errors))
    return rows


def write_manifest(campaign: Path, rows: list[dict]) -> Path:
    target = campaign / "manifest.csv"
    with target.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    return target


def run_magick(args: list[str]) -> None:
    subprocess.run(["magick", *args], check=True, capture_output=True)


def create_review_sheets(campaign: Path, rows: list[dict]) -> list[Path]:
    if shutil.which("magick") is None:
        print("Warning: ImageMagick not found; skipping review sheets.", file=sys.stderr)
        return []

    review = campaign / "review"
    review.mkdir(exist_ok=True)
    by_ratio: dict[str, list[Path]] = {ratio: [] for ratio in SPECS}
    for row in rows:
        by_ratio[row["ratio"]].append(campaign / row["filename"])

    outputs: list[Path] = []
    with tempfile.TemporaryDirectory(prefix="static-ad-review-") as tmp_name:
        tmp = Path(tmp_name)
        ratio_rows: list[Path] = []
        for ratio in SPECS:
            images = sorted(by_ratio[ratio])
            if not images:
                continue
            thumbs: list[Path] = []
            for index, image in enumerate(images):
                thumb = tmp / f"{ratio.replace('.', '-')}-{index:02d}.png"
                run_magick(
                    [
                        str(image),
                        "-thumbnail",
                        "280x280",
                        "-gravity",
                        "center",
                        "-background",
                        "#d8d0c4",
                        "-extent",
                        "300x300",
                        str(thumb),
                    ]
                )
                thumbs.append(thumb)
            ratio_sheet = review / f"all-concepts__{ratio}.jpg"
            run_magick([*(str(path) for path in thumbs), "+append", str(ratio_sheet)])
            outputs.append(ratio_sheet)

            row_copy = tmp / f"row-{ratio.replace('.', '-')}.jpg"
            shutil.copy2(ratio_sheet, row_copy)
            ratio_rows.append(row_copy)

        if ratio_rows:
            all_formats = review / "all-formats.jpg"
            run_magick([*(str(path) for path in ratio_rows), "-append", str(all_formats)])
            outputs.append(all_formats)
    return outputs


def create_zip(campaign: Path) -> Path:
    target = campaign.parent / f"{campaign.name}.zip"
    if target.exists():
        target.unlink()
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(campaign.rglob("*")):
            if path.is_file():
                archive.write(path, Path(campaign.name) / path.relative_to(campaign))
    with zipfile.ZipFile(target) as archive:
        bad = archive.testzip()
        if bad:
            raise ValueError(f"ZIP integrity check failed at {bad}")
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("campaign_directory", type=Path)
    parser.add_argument(
        "--allow-missing",
        action="store_true",
        help="Allow concepts without all four default ratios.",
    )
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="Validate without creating manifest, review sheets, or ZIP.",
    )
    args = parser.parse_args()

    campaign = args.campaign_directory.expanduser().resolve()
    try:
        rows = collect(campaign, args.allow_missing)
        if args.verify_only:
            print(f"Verified {len(rows)} assets in {campaign}")
            return 0
        manifest = write_manifest(campaign, rows)
        sheets = create_review_sheets(campaign, rows)
        archive = create_zip(campaign)
    except (OSError, ValueError, subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Verified assets: {len(rows)}")
    print(f"Manifest: {manifest}")
    print(f"Review sheets: {len(sheets)}")
    print(f"ZIP: {archive}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
