import os
import subprocess


head_ref = os.getenv("HEAD_REF", "master")

if __name__ == "__main__":
    subprocess.run(
        f"git diff --name-only origin/${head_ref}",
        shell=True
    )
