# Lightweight Container Demo

This repository contains a simple demonstration project that showcases how to build and containerize applications using Docker. It includes multiple example applications in different programming languages to illustrate cross-language development and container workflows.

## Features

- **Python 3.13 Flask Web Application**
  A lightweight Flask app demonstrating HTML form submission and dynamic image rendering inside a Docker container.

- **C++ Word Counting Example**
  A basic C++ console application that counts word occurrences in a text file, showcasing code style enforcement with clang-format and cpplint via pre-commit hooks.

- **Rust Word Counting Example**
  A similar word count utility implemented in Rust, illustrating idiomatic Rust code and toolchain integration.

- **Pre-commit Hooks for Code Quality**
  Automatic linting, formatting, and style checks configured for Python, C++, and Rust code using tools like ruff, black, isort, clang-format, and cpplint.

- **Cross-Platform Compatibility**
  Designed to run seamlessly on both Windows and Linux environments using Docker containers.

## Getting Started

1. Clone the repository.
2. Explore each language-specific example in the `src/` folder:
   - `example1/src/tremendous_app` for Python
   - `example2/src/rust_word_counter` for Rust
   - `example3/src/cpp_word_counter` for C++
3. Build and run the Docker containers as described in the project documentation.
