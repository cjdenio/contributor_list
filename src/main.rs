mod action;
mod github;
mod template;
mod readme;

use readme::Readme;

use template::render_template;

fn main() {
    let repo = action::repository();
    let contributors = github::get_contributors(&repo);

    let readme = Readme::new("/home/cjdenio/Documents/list-test/README.md");

    println!("{:?}", readme.contributors().unwrap());

    match contributors {
        Ok(x) => match render_template(&x) {
            Ok(x) => println!("{:?}", x),
            Err(x) => println!("{:?}", x),
        },
        Err(_) => (),
    }
}
