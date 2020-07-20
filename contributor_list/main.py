from jinja2 import Template
import requests
import pathlib
import re
import os
from os import path

r = requests.get(
    f"https://api.github.com/repos/{os.environ['GITHUB_REPOSITORY']}/contributors?per_page={os.getenv('INPUT_MAX_CONTRIBUTORS', '10')}",
    headers={"cache-control": "no-cache"},
)

if path.exists(".github/contributor_list_template.md"):
    file_path = pathlib.Path(".github/contributor_list_template.md").absolute()
else:
    file_path = pathlib.Path(__file__).parent.absolute().joinpath("default_template.md")

with open(file_path) as template_file:
    template = Template(template_file.read())

rendered = template.render(
    {"contributors": list(filter(lambda x: x["login"] != "actions-user", r.json()))}
)

with open("README.md") as _readme:
    readme = _readme.read()

if not "<!-- DO NOT REMOVE - contributor_list:start -->" in readme:
    print("Contributor list not found - creating it now! 🎉")
    with open("README.md", "a") as readme:
        readme.write(
            "\n<!-- DO NOT REMOVE - contributor_list:start -->\n"
            + rendered
            + "\n<!-- DO NOT REMOVE - contributor_list:end -->"
        )
else:
    readme = re.sub(
        "(?<=<!-- DO NOT REMOVE - contributor_list:start -->\n).+?(?=\n<!-- DO NOT REMOVE - contributor_list:end -->)",
        rendered,
        readme,
        flags=re.DOTALL,
    )
    with open("README.md", "w") as _readme:
        _readme.write(readme)

os.system('git config --global user.email "action@github.com"')
os.system('git config --global user.name "Publishing Bot"')
os.system("git add .")
os.system(f'git commit -m "{os.getenv("INPUT_COMMIT_MESSAGE")}"')
os.system("git push")
