import os
import subprocess
import logging
import json


git_context = os.getenv("GITHUB_CONTEXT")
git_context_json = json.loads(git_context)
event = git_context["event"]

if __name__ == "__main__":
    logging.info(f"""
    GITHUB_CONTEXT: {git_context}
    """)

    subprocess.run(
        f"echo {event}",
        shell=True
    )
