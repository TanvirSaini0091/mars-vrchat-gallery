#!/usr/bin/env python3
import argparse
import re
import shutil
from pathlib import Path


def rename_screenshots(input_dir: Path, output_dir: Path):
    """
    Batch rename VRChat screenshots by removing milliseconds and resolution.
    Example: VRChat_2026-06-04_22-35-28.329_3840x2160.png -> VRChat_2026-06-04_22-35-28.png
    """
    if not input_dir.is_dir():
        raise SystemExit(f"Input directory does not exist: {input_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)
    in_place = input_dir.resolve() == output_dir.resolve()

    # Pattern: VRChat_YYYY-MM-DD_HH-MM-SS.milliseconds_WIDTHxHEIGHT.png
    pattern = r"(VRChat_\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})\.\d+_\d+x\d+\.png$"

    renamed_count = 0
    copied_count = 0

    for file_path in sorted(input_dir.glob("VRChat_*.png")):
        filename = file_path.name

        match = re.match(pattern, filename)
        if match:
            new_name = match.group(1) + ".png"
            new_path = output_dir / new_name

            if new_path.exists():
                print(f"⚠️  Skipped (already exists): {filename} -> {new_name}")
            elif in_place:
                file_path.rename(new_path)
                print(f"✓ Renamed: {filename} -> {new_name}")
                renamed_count += 1
            else:
                shutil.copy2(file_path, new_path)
                print(f"✓ Copied renamed file: {filename} -> {new_name}")
                copied_count += 1
        else:
            print(f"⊘ Skipped (doesn't match pattern): {filename}")

    print(f"\nTotal renamed: {renamed_count}")
    print(f"Total copied: {copied_count}")
    print(f"Output folder: {output_dir.absolute()}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rename VRChat screenshots by removing milliseconds and resolution."
    )
    parser.add_argument(
        "--input",
        "--input-dir",
        "--source-dir",
        dest="input_dir",
        type=Path,
        default=Path("."),
        help="Directory containing source VRChat_*.png files.",
    )
    parser.add_argument(
        "--output",
        "--output-dir",
        dest="output_dir",
        type=Path,
        default=Path("."),
        help="Directory where renamed files will be written.",
    )
    args = parser.parse_args()

    rename_screenshots(args.input_dir, args.output_dir)


if __name__ == "__main__":
    main()
