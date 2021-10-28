import os
import subprocess


if __name__ == "__main__":
    subprocess.run(
        "git diff --name-only origin/${GITHUB_HEAD_REF}",
        shell=True
    )
