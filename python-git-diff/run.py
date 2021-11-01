import os
import subprocess
from io import StringIO
import json


git_context = os.getenv("GITHUB_CONTEXT", "")
io = StringIO(git_context)
git_context_json = json.load(io)
context_type = type(git_context_json)

if __name__ == "__main__":

    subprocess.run(
        f"echo {context_type}",
        shell=True
    )
