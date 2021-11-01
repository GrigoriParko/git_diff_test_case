import os
import subprocess
import json
import re


git_context = os.getenv("GITHUB_CONTEXT", "")
git_context_json = json.loads(git_context)
default_branch_match = re.match(r".*default_branch.*: (.*),.*", str(git_context_json))
if default_branch_match:
    default_branch = default_branch_match[0].replace('"', '')

if __name__ == "__main__":

    subprocess.run(
        f'echo "::debug::{default_branch}"',
        shell=True,
    )
