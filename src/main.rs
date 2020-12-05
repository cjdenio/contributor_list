mod action;
mod github;
mod template;

use template::render_template;

fn main() {
    let repo = action::repository();
    let contributors = github::get_contributors(&repo);

    match contributors {
        Ok(x) => match render_template(&x) {
            Ok(x) => println!("{:?}", x),
            Err(x) => println!("{:?}", x),
        },
        Err(_) => (),
    }
}
