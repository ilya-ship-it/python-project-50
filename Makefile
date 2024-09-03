package-install:
	python3 -m pip install --user --force-reinstall  dist/*.whl

install:
	poetry install

lint:
	poetry run flake8 gendiff

test: 
	poetry run pytest