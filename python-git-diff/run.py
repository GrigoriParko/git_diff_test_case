import os
import subprocess
import json


git_context = os.getenv("GITHUB_CONTEXT", "")
git_context_json = json.loads(git_context)

if __name__ == "__main__":

    subprocess.run(
        f"echo {git_context[:50]}",
        shell=True
    )
