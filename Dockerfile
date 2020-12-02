# Build the app
FROM rust:1.48-alpine

WORKDIR /usr/src/app

COPY . .

RUN cargo build --release

# Run the app in an Alpine container
FROM alpine:latest

RUN apk --no-cache add git

COPY --from=0 /usr/src/app/target/release/contributor_list /bin/contributor_list

CMD ["contributor_list"]
