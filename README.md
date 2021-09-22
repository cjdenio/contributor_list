<!-- DO NOT REMOVE - contributor_list:data:start:["cjdenio", "gleich"]:end -->
# 👥 Contributor List

GitHub Action to easily list contributors on your README!

## 🏁 Getting Started

In your repository, create a file named `contributor_list.yml` under `.github/workflows/`.
Paste the following content into it:

```yml
name: Contributor List
on:
  push:
    branches:
      - master
jobs:
  contributor_list:
    name: Contributor List
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@master
      - uses: docker://cjdenio/contributor_list:latest
```

Push to the repo, and your contributor list has been created! 🎉

## ↕️ Moving the contributor list

Don't want it at the end of the README? That's OK! Just move it to the place you'd like. **Make sure you move the two `<!-- DO NOT REMOVE -->` comments along with it!**

## 📝 Writing a custom template

Don't like the default look? You can write a custom [Jinja](https://jinja.palletsprojects.com/) template, then place it in the `.github/contributor_list_template.md` file. [Here's the default one](https://raw.githubusercontent.com/cjdenio/contributor_list/master/contributor_list/default_template.md), for inspiration.

`contributors` is an array that looks like this (already sorted by number of contributions, by the way):

```json
[
  {
    "login": "octocat",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "html_url": "https://github.com/octocat",
    "contributions": 32
  }
]
```

## ⚙️ Configuration

You can customize your contributor list with various options! Below is an example: (they're all optional, by the way)

```yaml
name: Contributor List
on:
  push:
    branches:
      - master
jobs:
  contributor_list:
    name: Contributor List
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@master
      - uses: docker://cjdenio/contributor_list:latest
        with:
          commit_message: 📝 Update contributors list
          # Max number of contributors to display on the README
          max_contributors: 5 # Default: 10
          # This enables showing contribution numbers on the README.
          # ⚠️ THIS WILL PUSH TO THE REPO AFTER EVERY COMMIT ⚠️
          show_numbers: true # Default: false
          # Markdown heading level for the contributors section
          header_level: 3 # Default: 2
```

## 🐛 Known Issues

- [**Contributor List won't work if your default branch is protected.**](https://github.com/cjdenio/contributor_list/issues/6)

<!-- DO NOT REMOVE - contributor_list:start -->
## 👥 Contributors


- **[@cjdenio](https://github.com/cjdenio)**

- **[@gleich](https://github.com/gleich)**

<!-- DO NOT REMOVE - contributor_list:end -->
