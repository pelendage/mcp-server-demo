fmt:
	uv run isort .
	uv run black .
	uv run ruff check . --fix

verify:
	uv run isort . --check
	uv run black . --check
	uv run ruff check .