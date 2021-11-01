import os
import subprocess
import logging


git_context = os.getenv("GITHUB_CONTEXT")
# base_ref = git_context

if __name__ == "__main__":
    logging.info(f"""
    GITHUB_CONTEXT: {git_context}
    """)

    subprocess.run(
        f"echo `{git_context}`",
        shell=True
    )
