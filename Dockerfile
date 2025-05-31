
#Here we'll create the venv needed for our app
# If we change the pyproject.toml file this stage will re run when we build the image

FROM python:3.13-slim
WORKDIR /app
EXPOSE 8080
RUN mkdir /memes
RUN python -m venv /app-venv
RUN /app-venv/bin/python -m pip install -U setuptools wheel --verbose
COPY src src
COPY pyproject.toml pyproject.toml
COPY requirements.txt requirements.txt
RUN /app-venv/bin/pip install . --verbose
RUN /app-venv/bin/tremendous-app --help # just make sure it launches!

ENTRYPOINT ["/app-venv/bin/tremendous-app"]

