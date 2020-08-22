from util import (
    getTemplate,
    writeToReadme,
    getStoredContributors,
    setStoredContributors,
)
import util
import requests
import os
from os import path
import json

showNumbers = os.getenv("INPUT_SHOW_NUMBERS", "false").lower() == "true"


def commit():
    if not os.getenv("DEV") == "true":
        util.commit(os.getenv("INPUT_COMMIT_MESSAGE", "Update contributors list"))
    else:
        print("Running in dev mode, not committing")


def stripToLogin(contributors):
    return list(map(lambda x: x["login"], contributors))


r = requests.get(
    f"https://api.github.com/repos/{os.environ['GITHUB_REPOSITORY']}/contributors?per_page={os.getenv('INPUT_MAX_CONTRIBUTORS', '10')}",
    headers={"cache-control": "no-cache"},
)

contributors = list(filter(lambda x: x["login"] != "actions-user", r.json()))
if not showNumbers:

    def removeNumbers(x: dict):
        x.pop("contributions")
        return x

    contributors = list(map(removeNumbers, contributors))

rendered = getTemplate(contributors)

storedContributors = getStoredContributors()

# Only update list if
#   a) the stored contributor list isn't there
#   b) the user wants to display contribution numbers
#   c) the list of contributors has been updated since the last push
if (
    (storedContributors is None)
    or showNumbers
    or (storedContributors != stripToLogin(contributors))
):
    if storedContributors != stripToLogin(contributors):
        print(f"Current contributors in README: {json.dumps(storedContributors)}\nActual repo contributors: {json.dumps(stripToLogin(contributors))}")

    setStoredContributors(stripToLogin(contributors))
    writeToReadme(rendered)
    commit()
else:
    print("Nothing to change!")
