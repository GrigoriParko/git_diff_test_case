import os
import subprocess
import logging


head_ref = os.getenv("HEAD_REF", "master")
base_ref = os.getenv("BASE_REF", "origin")

if __name__ == "__main__":
    logging.info(f"""
    GITHUB_HEAD_REF: {head_ref}
    GITHUB_BASE_REF: {base_ref}
    """)
    subprocess.run(
        f"git diff --name-only `origin...master`",
        shell=True
    )
