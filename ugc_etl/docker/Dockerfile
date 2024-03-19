FROM python:3.11

WORKDIR /app
ENV PYTHONPATH=/app

RUN apt-get update \
    && apt-get install -y netcat-traditional \
    && pip install --upgrade pip \
    && pip install --no-cache-dir poetry

COPY ./poetry.lock ./poetry.lock
COPY ./pyproject.toml ./pyproject.toml
COPY ./docker/docker-entrypoint.sh ./docker-entrypoint.sh

RUN poetry config virtualenvs.create false \
    && poetry install --no-cache --no-root

COPY ./data ./data
COPY ./Makefile ./Makefile

RUN ["chmod", "o+x", "./docker-entrypoint.sh"]

COPY ./src ./src

#ENTRYPOINT ["python", "./src/main.py"]
ENTRYPOINT ["./docker-entrypoint.sh", "kafka-0:9092", "--", "python", "./src/main.py"]