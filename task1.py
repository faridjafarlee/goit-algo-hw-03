import argparse
import shutil
from pathlib import Path


def copy_and_sort(src: Path, dest: Path) -> None:
    try:
        for item in src.iterdir():
            try:
                if item.is_dir():
                    copy_and_sort(item, dest)
                elif item.is_file():
                    ext = item.suffix.lower().lstrip(".") or "no_extension"
                    target_dir = dest / ext
                    target_dir.mkdir(parents=True, exist_ok=True)

                    target_file = target_dir / item.name

                    if target_file.exists():
                        stem = target_file.stem
                        suffix = target_file.suffix
                        i = 1
                        while True:
                            candidate = target_dir / f"{stem}({i}){suffix}"
                            if not candidate.exists():
                                target_file = candidate
                                break
                            i += 1

                    shutil.copy2(item, target_file)

            except PermissionError as e:
                print(f"[SKIP: permission] {item} -> {e}")
            except OSError as e:
                print(f"[SKIP: os error] {item} -> {e}")

    except FileNotFoundError:
        raise
    except PermissionError as e:
        raise PermissionError(f"No access to directory: {src}") from e


def parse_args():
    parser = argparse.ArgumentParser(
        description="Recursively copy files from source directory to destination, sorting by extension."
    )
    parser.add_argument("source", help="Path to source directory")
    parser.add_argument(
        "destination",
        nargs="?",
        default="dist",
        help="Path to destination directory (default: dist)",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    src = Path(args.source).resolve()
    dest = Path(args.destination).resolve()

    if not src.exists() or not src.is_dir():
        raise ValueError(f"Source must be an existing directory: {src}")

    dest.mkdir(parents=True, exist_ok=True)

    copy_and_sort(src, dest)
    print(f"Done. Files copied from '{src}' to '{dest}' and sorted by extension.")


if __name__ == "__main__":
    main()
