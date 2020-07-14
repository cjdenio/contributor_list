from jinja2 import Template
import requests
import pathlib

r = requests.get(
    "https://api.github.com/repos/Standard-Structure/Standard-Structure/contributors"
)

file_path = pathlib.Path(__file__).parent.absolute().joinpath("default_template.md")

with open(file_path) as template_file:
    template = Template(template_file.read())

print(template.render({"contributors": r.json()}))
