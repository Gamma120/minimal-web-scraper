.PHONY: docs

pre-commit: linting docs
	poetry install
	tox

init:
	pyenv local 3.10 3.11
	poetry shell

flake8:
	flake8

mypy:
	mypy --strict

black:
	black --check --diff src/

linting: flake8 mypy black

docs:
	cd docs/ && make linkcheck && make coverage && make html