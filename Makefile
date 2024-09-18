# Load the environment variables
include .env
export $(shell sed 's/=.*//' .env)

.PHONY: venv install run db-migrate db-downgrade migration-history db-revision test lint clean

venv:
	python3 -m venv venv && \
	. venv/bin/activate && \
	pip install -r requirements.txt

install: venv
	npm install

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

watch:
	npm run watch:tailwindcss

migrations:
	alembic -c app/models/alembic.ini revision --autogenerate

migrate:
	alembic -c app/models/alembic.ini upgrade head

downgrade:
	alembic -c app/models/alembic.ini downgrade -1

history:
	alembic -c app/models/alembic.ini history