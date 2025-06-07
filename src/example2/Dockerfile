FROM rust:1.85 as build-stage

WORKDIR /usr/workspace
COPY src src

WORKDIR /usr/workspace/src/rust_word_counter

RUN cargo build --release
RUN mkdir bin
RUN cp target/release/rust_word_counter bin/ --verbose

FROM debian:bookworm-slim as deploy-app-stage
COPY --from=build-stage /usr/workspace/src/rust_word_counter/bin/rust_word_counter /usr/local/bin/rust_word_counter
RUN rust_word_counter --help
ENTRYPOINT ["rust_word_counter"]
CMD ["--help"]
