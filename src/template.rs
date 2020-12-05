use super::{action, github};
use tera::{Context, Tera};

use std::fs;
use std::path::Path;

pub fn render_template(contributors: &Vec<github::Contributor>) -> Result<String, String> {
    // I'm using include_str instead of std::fs because it includes the file in the compiled binary
    let default_template = include_str!("../static/default_template.md");

    let template = match user_defined_template() {
        Some(x) => x,
        None => default_template.to_string(),
    };

    let mut tera = Tera::default();

    let mut context = Context::new();
    context.insert("contributors", contributors);

    return tera
        .render_str(&template, &context)
        .map_err(|e| e.to_string());
}

fn user_defined_template() -> Option<String> {
    fs::read_to_string(
        Path::new(&action::github_workspace()).join(".github/contributor_list_template.md"),
    )
    .ok()
}
