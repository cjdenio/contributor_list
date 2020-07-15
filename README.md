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
      - uses: cjdenio/contributor_list@master

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
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false,
    "contributions": 32
  }
]
```

## 👀 Live Example
<!-- DO NOT REMOVE - contributor_list:start -->
## 👥 Contributors


- **[@cjdenio](https://github.com/cjdenio)** (11 contributions)

- **[@actions-user](https://github.com/actions-user)** (1 contribution)

<!-- DO NOT REMOVE - contributor_list:end -->