# Stage 1: Build the Rust application using the official Rust image
FROM rust:1.85 as build-stage

# Set the working directory for the build process
WORKDIR /usr/workspace

# Copy the application source code into the container
COPY src src

# Navigate to the Rust project directory
WORKDIR /usr/workspace/src/rust_word_counter

# Compile the Rust app in release mode (optimized)
RUN cargo build --release

# Create a directory to hold the built binary
RUN mkdir bin

# Copy the compiled binary to the bin directory for easier access
RUN cp target/release/rust_word_counter bin/ --verbose

# Stage 2: Create a lightweight runtime image using Debian
FROM debian:bookworm-slim as deploy-app-stage

# Copy the compiled binary from the build stage into the runtime image
COPY --from=build-stage /usr/workspace/src/rust_word_counter/bin/rust_word_counter /usr/local/bin/rust_word_counter

# (Optional) Run the binary with --help to verify it works (could be removed for faster builds)
RUN rust_word_counter --help

# Set the default entrypoint to run the Rust binary
ENTRYPOINT ["rust_word_counter"]

# Provide a default argument to display help info (can be overridden)
CMD ["--help"]
