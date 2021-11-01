import os
import subprocess
import re


git_context = os.getenv("GITHUB_CONTEXT", "")
IMPORTANT_CONTEXT_PARTS = ["ref", "default_branch"]

context_dict = dict()
for k in IMPORTANT_CONTEXT_PARTS:
    k_match = re.search(f"{k}:\s(?P<{k}>.+?)(?=,)", git_context)
    if k_match:
        context_dict[k] = k_match.groupdict()[k]

if __name__ == "__main__":

    subprocess.run(
        f'echo "::debug::{context_dict["ref"]}"',
        shell=True,
    )
