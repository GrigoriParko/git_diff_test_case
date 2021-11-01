import os
import subprocess
import logging
import json


git_context = os.getenv("GITHUB_CONTEXT")
git_context_json = json.loads(git_context)
context_type = type(git_context_json)

if __name__ == "__main__":

    subprocess.run(
        f"echo {context_type}",
        shell=True
    )
