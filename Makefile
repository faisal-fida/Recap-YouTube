# Load the environment variables
include .env
export $(shell sed 's/=.*//' .env)

.PHONY: venv install run db-migrate db-downgrade migration-history db-revision test lint clean

venv:
	poetry install

install: venv
	poetry run npm install

run:
	poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

migrations:
	poetry run alembic -c app/models/alembic.ini revision --autogenerate

migrate:
	poetry run alembic -c app/models/alembic.ini upgrade head

downgrade:
	poetry run alembic -c app/models/alembic.ini downgrade -1

history:
	poetry run alembic -c app/models/alembic.ini history