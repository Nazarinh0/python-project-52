install:
	@poetry install

migrate:
	@poetry run python manage.py migrate

start:
	@poetry run python manage.py runserver

shell:
	@poetry run python manage.py shell_plus

lint:
	@poetry run flake8 task_manager --exclude=migrations,settings.py

test:
	@poetry run python manage.py test

test-coverage:
	@poetry run coverage run --source='.' manage.py test
	@poetry run coverage report
	@poetry run coverage xml

requirements.txt: poetry.lock
	@poetry export -f requirements.txt --output requirements.txt --without-hashes