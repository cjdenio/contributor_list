use regex::Regex;
use std::{fs, io};

pub struct Readme {
    pub path: String,
}

impl Readme {
    pub fn new(path: &str) -> Readme {
        Readme {
            path: path.to_string(),
        }
    }

    fn read(&self) -> Result<String, String> {
        fs::read_to_string(&self.path).map_err(|_| format!("Unable to read file at {}", self.path))
    }

    /// Lists the contributors currently listed on the README
    pub fn contributors(&self) -> Result<Option<Vec<String>>, String> {
        let file = self.read()?;

        let re =
            Regex::new(r"<!-- DO NOT REMOVE - contributor_list:data:start:(.+):end -->").unwrap();
        Ok(match re.captures(&file) {
            Some(x) => serde_json::from_str::<Vec<String>>(x.get(1).unwrap().as_str()).ok(),
            None => None,
        })
    }
}
