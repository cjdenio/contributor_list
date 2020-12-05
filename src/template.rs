use super::github;
use tera::{Context, Tera};

pub fn render_template(contributors: &Vec<github::Contributor>) -> Result<String, String> {
    // I'm using include_str instead of std::fs because it includes the file in the compiled binary
    let template = include_str!("../static/default_template.md");

    let mut tera = Tera::default();

    let mut context = Context::new();
    context.insert("contributors", contributors);

    return tera
        .render_str(template, &context)
        .map_err(|e| e.to_string());
}
