mod action;
mod github;

fn main() {
    let repo = action::repository();
    let contributors = github::get_contributors(&repo);

    match contributors {
        Ok(x) => println!("{:?}", x.iter().map(|v| &v.login).collect::<Vec<&String>>()),
        Err(x) => println!("{}", x),
    }
}
