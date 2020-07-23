from jinja2 import Template
from os import path
import pathlib
from typing import List
import re
import json


def getTemplate(contributors: List[dict]) -> str:
    if path.exists(".github/contributor_list_template.md"):
        file_path = pathlib.Path(".github/contributor_list_template.md").absolute()
    else:
        file_path = (
            pathlib.Path(__file__).parent.absolute().joinpath("default_template.md")
        )

    with open(file_path) as template_file:
        template = Template(template_file.read())

    return template.render({"contributors": contributors})


def writeToReadme(rendered: str) -> None:
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


def commit(commit_name: str) -> None:
    os.system('git config --global user.email "action@github.com"')
    os.system('git config --global user.name "Publishing Bot"')
    os.system("git add .")
    os.system(f'git commit -m "{commit_name}"')
    os.system("git push")


def getStoredContributors():
    with open("README.md") as _readme:
        readme = _readme.read()
    match = re.search(
        "<!-- DO NOT REMOVE - contributor_list:data:start:(.+):end -->", readme
    )
    if match is None:
        return None
    parsed = json.loads(match.group(1))

    return parsed


def setStoredContributors(contributors):
    with open("README.md") as _readme:
        readme = _readme.read()
    match = re.search(
        "<!-- DO NOT REMOVE - contributor_list:data:start:(.+):end -->", readme
    )
    if match is None:
        readme = f"<!-- DO NOT REMOVE - contributor_list:data:start:{json.dumps(contributors)}:end -->\n{readme}"
    else:
        readme = re.sub(
            "(?<=<!-- DO NOT REMOVE - contributor_list:data:start:).+(?=:end -->)",
            json.dumps(contributors),
            readme,
        )

    with open("README.md", "w") as _readme:
        _readme.write(readme)
