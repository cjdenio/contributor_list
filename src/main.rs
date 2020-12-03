mod github;
mod action;

fn main() {
    let contributors = github::get_contributors(&action::repository());

    match contributors {
        Ok(x) => println!("{:?}", x[0].login),
        Err(x) => println!("{}", x)
    }
}
