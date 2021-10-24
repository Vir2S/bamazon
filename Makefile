.PHONY: all \
		setup \
		run \
		static \
		db \
		flake8 \
		mypy \
		black

venv/bin/activate: ## alias for virtual environment
	python -m venv venv

setup: venv/bin/activate ## project setup
	. venv/bin/activate; pip install pip wheel setuptools
	. venv/bin/activate; pip install -r requirements.txt

run: venv/bin/activate ## Run
	. venv/bin/activate; python manage.py runserver

static: venv/bin/activate ## Static Collect
	. venv/bin/activate; python manage.py collectstatic

db: venv/bin/activate ## Run Migrations
	. venv/bin/activate; python manage.py migrate

flake8: venv/bin/activate ## Run Flake8
	. venv/bin/activate; flake8 .

mypy: venv/bin/activate ## Run MyPy
	. venv/bin/activate; mypy .

black: venv/bin/activate ## Run Black
	. venv/bin/activate; black .