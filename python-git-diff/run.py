import os
import subprocess
import json
import re


git_context = os.getenv("GITHUB_CONTEXT", "")
git_context_json = json.loads(git_context)
default_branch = re.match(".*default_branch: (.*),", str(git_context_json))

if __name__ == "__main__":

    subprocess.run(
        f'echo "::debug::{default_branch}"',
        shell=True,
    )
