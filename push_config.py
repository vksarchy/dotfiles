
#!/usr/bin/env python3

import subprocess
import shutil
from pathlib import Path
from datetime import datetime
import stat

HOME = Path.home()
SOURCE_CONFIG = HOME / ".config"
REPO_DIR = HOME / "dotfiles"
DEST_CONFIG = REPO_DIR / "config"


def run(cmd, cwd=None):
    print(f"▶ {cmd}")
    subprocess.run(cmd, shell=True, check=True, cwd=cwd)


def ignore_special_files(src, names):
    ignored = []
    for name in names:
        path = Path(src) / name
        try:
            mode = path.lstat().st_mode
            if stat.S_ISSOCK(mode):
                ignored.append(name)  # ignore socket files
        except FileNotFoundError:
            ignored.append(name)
    return ignored


def sync_config():
    if DEST_CONFIG.exists():
        shutil.rmtree(DEST_CONFIG)

    shutil.copytree(
        SOURCE_CONFIG,
        DEST_CONFIG,
        symlinks=True,
        ignore=ignore_special_files,
        ignore_dangling_symlinks=True,
    )

    print("✔ Synced ~/.config (sockets skipped)")


def git_push():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    run("git add .", cwd=REPO_DIR)
    run(f'git commit -m "Update config: {timestamp}"', cwd=REPO_DIR)
    run("git push", cwd=REPO_DIR)


def main():
    sync_config()
    git_push()
    print("🚀 Config pushed to GitHub successfully")


if __name__ == "__main__":
    main()
