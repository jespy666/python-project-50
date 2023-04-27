install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

rec:
	asciinema rec

package-install:
	python3 -m pip install .