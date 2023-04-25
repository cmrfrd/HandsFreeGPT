#!/bin/bash
# Run all checks and tests in the ci pipeline
poetry run ruff --target-version py310 --fix $(git ls-files '*.py')
poetry run black  --target-version py310 $(git ls-files '*.py' '.ipynb')
poetry run isort $(git ls-files '*.py')
poetry run flake8 $(git ls-files '*.py')
poetry run pydocstyle $(git ls-files 'cvml/dagster/**/*.py' 'cvml/utils/*.py' 'cvml/models/*.py') --verbose --convention=google --add-ignore=D104
poetry run pylint $(git ls-files '*.py')
poetry run mypy $(git ls-files '*.py')