POETRY = ./.venv/bin/poetry


venv: ##@Env Init venv and install poetry dependencies
	@rm -rf .venv || true && \
	python3.11 -m venv .venv && \
	.venv/bin/pip install poetry && \
	${POETRY} install --no-root


run_dev:
	docker compose -f docker-compose.yaml -f docker-compose.dev.yaml up -d

stop_dev:
	docker compose -f docker-compose.yaml -f docker-compose.dev.yaml down -v

build_image:
	docker build -t ugc_service -f ./docker/Dockerfile .
