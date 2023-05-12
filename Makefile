install:
	@poetry install

migrate:
	@poetry run python manage.py migrate

start:
	@poetry run python manage.py runserver

shell:
	@poetry run python manage.py shell

lint:
	@poetry run flake8 task_manager --exclude=migrations,settings.py

test:
	@poetry run coverage run --source='.' manage.py test

test-coverage:
	@poetry run coverage report

test-coverage-report-xml:
	@poetry run coverage xml
