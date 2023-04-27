gendiff:
	poetry run gendiff -h

build:
	poetry build

publish:
	poetry publish --dry-run

install:
	python3 -m pip install .

rec:
	asciinema rec

lint:
	poetry run flake8 gendiff