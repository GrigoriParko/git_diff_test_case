import os
import subprocess
import logging


git_context = os.getenv("GITHUB_CONTEXT", )

if __name__ == "__main__":
    logging.info(f"""
    GITHUB_CONTEXT: {git_context}
    """)

    subprocess.run(
        f"git diff --name-only `{git_context}`",
        shell=True
    )
