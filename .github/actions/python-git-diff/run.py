import os
import subprocess


base = os.getenv("BASE")
head = os.getenv("HEAD")
patterns = os.getenv("PATTERNS")
ppds_py = os.getenv("PPDS_PY_DIR")


if __name__ == "__main__":
    subprocess.run(
        f"git diff --name-only origin/${head}",
        shell=True
    )
