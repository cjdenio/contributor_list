from jinja2 import Template
import requests
import pathlib
import re
import os

r = requests.get(
    f"https://api.github.com/repos/{os.environ["GITHUB_REPOSITORY"]}/contributors"
)

file_path = pathlib.Path(__file__).parent.absolute().joinpath(
    "default_template.md")

with open(file_path) as template_file:
    template = Template(template_file.read())

rendered = template.render({"contributors": r.json()})

with open("README.md") as _readme:
    readme = _readme.read()

if not "<!-- DO NOT REMOVE - contributor_list:start -->" in readme:
    print("Contributor list not found - creating it now! 🎉")
    with open("README.md", "a") as readme:
        readme.write("\n<!-- DO NOT REMOVE - contributor_list:start -->\n" +
                     rendered + "\n<!-- DO NOT REMOVE - contributor_list:end -->")
else:
    readme = re.sub('(?<=<!-- DO NOT REMOVE - contributor_list:start -->\n).+?(?=\n<!-- DO NOT REMOVE - contributor_list:end -->)',
                    rendered, readme, flags=re.DOTALL)
    with open("README.md", "w") as _readme:
        _readme.write(readme)

os.system('git config --global user.email "action@github.com"')
os.system('git config --global user.name "Publishing Bot"')
os.system('git add .')
os.system('git commit -m "Update contributors list"')
os.system('git push')
