#!/usr/bin/env bash
REF=master

.PHONY: run
run:
	pipenv run python manage.py runserver

# remove artifacts from build and dev tools
.PHONY: clean
clean:
	find . -type f \( -name '*.pyc' \) -delete  # find and delete regular files
	find . -type d \( -name '.pytest_cache' -o -name '__pycache__' -o -name '.mypy_cache' \) -prune -exec rm -rf {} \;

# run lint and type checks
.PHONY: lint
lint:
	pipenv run flake8 .

# run type checks
.PHONY: mypy
mypy:
	pipenv run mypy .

# run all unit tests
.PHONY: test-unit
test-unit: clean
	DJANGO_SETTINGS_MODULE=sadcp.settings_test pipenv run python -m pytest ./sadcp/tests/unit --cov-fail-under=92

# run all integration tests
.PHONY: test-int
test-int: clean
	DJANGO_SETTINGS_MODULE=sadcp.settings_test pipenv run python -m pytest ./sadcp/tests/integration --cov-fail-under=93

# run all lint, type checks, unit and integration tests
.PHONY: test
test: lint mypy test-unit test-int

# install all python modules required for staging/production
.PHONY: install
install:
	pipenv install

# install all python modules required for development
.PHONY: install-dev
install-dev:
	pipenv install --dev

# remove all installed python modules
.PHONY: uninstall
uninstall:
	pipenv uninstall --all

# helper to git fetch the given ref (branch or commit)
.PHONY: checkout
checkout:
	git fetch origin
	git checkout $(REF)

# checkout the given ref (branch or commit), run tests, and deploy to heroku
# - deploy your local master branch with `make deploy`
# - deploy any other local branch with `make deploy REF={branchname}`
# - deploy a specific commit with `make deploy REF={SHA}`
.PHONY: deploy
deploy: checkout test
	git push heroku $(REF):master
