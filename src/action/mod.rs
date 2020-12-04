use std::env;

pub fn input(input: &str) -> Option<String> {
    env::var(format!("INPUT_{}", input.to_uppercase())).ok()
}

/// Gets the GitHub repository the action is currently running on, in owner/name format
pub fn repository() -> String {
    env::var("GITHUB_REPOSITORY").expect("Not running in a GitHub Actions environment")
}
