package-install:
	python3 -m pip install --user --force-reinstall  dist/*.whl

lint:
	poetry run flake8 gendiff