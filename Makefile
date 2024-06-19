install:
	poetry install

makemigrations:
	poetry run ./manage.py makemigrations

migrate:
	poetry run ./manage.py migrate

dev:
	python3 manage.py runserver

test:
	poetry run coverage run manage.py test

lint:
	poetry run flake8

