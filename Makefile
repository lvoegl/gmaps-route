.PHONY: check
check:
	poetry run black --diff --check .
	poetry run isort --check-only .
	poetry run mypy .

.PHONY: mypy
mypy:
	poetry run mypy .

.PHONY: isort
isort:
	poetry run isort .

.PHONY: black
black:
	poetry run black .

.PHONY: format
format: mypy isort black
