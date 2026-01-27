#!/usr/bin/env python3
import subprocess
import shutil
from pathlib import Path
from datetime import datetime

HOME = Path.home()
REPO_DIR = HOME / "dotfiles"

ESSENTIAL_CONFIGS = [
    "hypr",
    "waybar",
    "rofi",
    "dunst",
    "swaylock",
    "kitty",
    "fish",
    "tmux",
    "git",
    "yazi",
    "btop",
    "kanata",
    "mimeapps.list",
    "user-dirs.dirs",
]

DOOM_ONLY = ["config.el", "init.el", "packages.el", "themes/", "snippets/"]


def run(cmd, cwd=None, check=True):
    print(f"▶ {cmd}")
    subprocess.run(cmd, shell=True, check=check, cwd=cwd)


def sync_item(name):
    src = HOME / ".config" / name
    dst = REPO_DIR / "config" / name

    if not src.exists():
        print(f"⊘ {name}")
        return

    if dst.exists():
        shutil.rmtree(dst) if dst.is_dir() else dst.unlink()

    dst.parent.mkdir(parents=True, exist_ok=True)

    if src.is_dir():
        shutil.copytree(src, dst, symlinks=True, ignore_dangling_symlinks=True)
    else:
        shutil.copy2(src, dst)

    print(f"✔ {name}")


def sync_doom():
    """Only sync Doom config files, not packages"""
    doom_src = HOME / ".config" / "doom"
    doom_dst = REPO_DIR / "config" / "doom"

    if not doom_src.exists():
        print("⊘ doom")
        return

    doom_dst.mkdir(parents=True, exist_ok=True)

    for item in DOOM_ONLY:
        src = doom_src / item
        dst = doom_dst / item

        if not src.exists():
            continue

        if dst.exists():
            shutil.rmtree(dst) if dst.is_dir() else dst.unlink()

        if src.is_dir():
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)

    print("✔ doom (config only)")


def main():
    print("🔄 Syncing essential configs...\n")

    for config in ESSENTIAL_CONFIGS:
        if config not in ["mimeapps.list", "user-dirs.dirs"]:
            sync_item(config)

    # Special handling for Doom
    sync_doom()

    # Copy essential files
    for file in ["mimeapps.list", "user-dirs.dirs"]:
        sync_item(file)

    print("\n📦 Committing...\n")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    run("git add .", cwd=REPO_DIR)

    # Check for changes
    result = subprocess.run("git diff --staged --quiet", shell=True, cwd=REPO_DIR)
    if result.returncode == 0:
        print("⊘ No changes")
        return

    run(f'git commit -m "Update: {timestamp}"', cwd=REPO_DIR)

    # Check if remote exists
    result = subprocess.run(
        "git remote get-url origin",
        shell=True,
        cwd=REPO_DIR,
        capture_output=True,
        check=False,
    )

    if result.returncode == 0:
        print("\n📤 Pushing...\n")
        run("git push -u origin main", cwd=REPO_DIR, check=False)
    else:
        print("\n⚠ No remote configured. Set it up with:")
        print(f"  cd {REPO_DIR}")
        print("  git remote add origin https://github.com/YOUR_USERNAME/dotfiles.git")
        print("  git push -u origin main")

    print("\n🚀 Done!")


if __name__ == "__main__":
    main()
