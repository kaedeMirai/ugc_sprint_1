FROM python:3.11

WORKDIR /app
ENV PYTHONPATH=/app

RUN pip install --upgrade pip \
    && pip install --no-cache-dir poetry

COPY ./README.md ./README.md
COPY ./poetry.lock ./poetry.lock
COPY ./pyproject.toml ./pyproject.toml

RUN poetry config virtualenvs.create false \
    && poetry install --no-cache --no-root

COPY ./docker/docker-entrypoint.sh ./docker-entrypoint.sh
COPY ./Makefile ./Makefile

COPY ./src ./

RUN chmod o+x /app/docker-entrypoint.sh

ENTRYPOINT ["/app/docker-entrypoint.sh"]