# Use the official slim Python 3.13 image as the build environment
FROM python:3.13-slim AS build-app

# Set the working directory inside the image to /app
WORKDIR /app

# Create a virtual environment in a separate directory for isolation
RUN python -m venv /app-venv

# Copy the application source code into the container image
COPY src src

# Copy the project metadata and dependency files into the image
COPY pyproject.toml pyproject.toml
COPY requirements.txt requirements.txt

# Install the app and its dependencies using the virtual environment
RUN /app-venv/bin/pip install . --verbose

# Start a new, clean layer for the final runtime image
FROM python:3.13-slim AS deployed-app

# Create a directory inside the container for storing mounted meme files
RUN mkdir /memes

# Copy the previously built virtual environment from the build stage into the runtime image
COPY --from=build-app /app-venv /app-venv

# (Optional) Run the app with --help to verify that it was installed correctly
RUN /app-venv/bin/tremendous-app --help

# Define the container entrypoint so that the app runs automatically on container start
ENTRYPOINT ["/app-venv/bin/tremendous-app"]
