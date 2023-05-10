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