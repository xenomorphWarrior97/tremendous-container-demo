FROM python:3.13-slim

WORKDIR /app

RUN mkdir /memes
RUN python -m venv /app-venv
RUN /app-venv/bin/python -m pip install -U setuptools wheel --verbose

COPY src src
COPY pyproject.toml pyproject.toml
COPY requirements.txt requirements.txt

RUN /app-venv/bin/pip install . --verbose
RUN /app-venv/bin/tremendous-app --help # just make sure it launches!

ENTRYPOINT ["/app-venv/bin/tremendous-app"]

