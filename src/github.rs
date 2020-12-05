use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Debug)]
pub struct Contributor {
    pub login: String,
    pub avatar_url: String,
    pub contributions: Option<i32>,
    pub html_url: String,
}

pub fn get_contributors(repo: &str) -> Result<Vec<Contributor>, String> {
    let url = &format!("https://api.github.com/repos/{}/contributors", repo);

    let client = reqwest::blocking::Client::new();
    let resp = client
        .get(url)
        .header("User-Agent", "cjdenio/contributor_list")
        .send()
        .map_err(|v| v.to_string())?;

    if !resp.status().is_success() {
        return Err(resp
            .text()
            .unwrap_or(String::from("non-success status code")));
    }

    let contributors = resp.json::<Vec<Contributor>>().map_err(|v| v.to_string())?;

    Ok(contributors)
}
