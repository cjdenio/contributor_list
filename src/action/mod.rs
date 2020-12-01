use std::env;

pub fn input(input: &'static str) -> Option<String> {
    env::var(format!("INPUT_{}", input.to_uppercase())).ok()
}
