fmt:
	uv run black .
	uv run ruff check . --fix

lint:
	uv run black . --check
	uv run ruff check .