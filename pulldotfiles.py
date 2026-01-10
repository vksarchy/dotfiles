
#!/usr/bin/env python3

import shutil
from pathlib import Path

HOME = Path.home()
REPO = HOME / "dotfiles"

PAIRS = [
    (REPO / "config", HOME / ".config"),
    (REPO / "local/bin", HOME / ".local/bin"),
]

def sync(src, dst):
    if not src.exists():
        return
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        target = dst / item.name
        if target.exists():
            target.unlink() if target.is_file() else shutil.rmtree(target)
        shutil.copytree(item, target) if item.is_dir() else shutil.copy2(item, target)

def main():
    for src, dst in PAIRS:
        sync(src, dst)
        print(f"✔ Restored {dst}")
    print("🚀 Dotfiles restored")

if __name__ == "__main__":
    main()
