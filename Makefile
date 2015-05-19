PYTHON = $(shell which python3.4)
ENV = $(CURDIR)/env
PROJECT = mtg_django
COVERAGE = $(ENV)/bin/coverage
COVERAGE_OPTS = --rcfile=coverage.cfg
TEST = $(MANAGE) test
MANAGE = ./manage.py

virtual-env:
	virtualenv --python=$(PYTHON) env

env: virtual-env
	env/bin/pip3 install -r requirements.txt

make bpython-env: test-env
	env/bin/pip3 install bpython -i http://pypi.python.org/pypi

clean:
	rm -rf env
	find . -iname '*.pyc' -exec rm {} \;

pip-freeze:
	$(ENV)/bin/pip3 freeze > requirements.txt

coverage:
	$(ENV)/bin/pip3 install -r requirements.txt

test:
	$(ENV)/bin/python3 $(TEST)

unit:
	$(ENV)/bin/python3 $(TEST) deckbuilder

func:
	$(ENV)/bin/python3 $(TEST) functional_tests

test-coverage: coverage
	$(COVERAGE) erase
	. $(ENV)/bin/activate; $(COVERAGE) run $(COVERAGE_OPTS) -L $(TEST)
	$(COVERAGE) report -m $(COVERAGE_OPTS)

coverage-html: test-coverage
	$(COVERAGE) html $(COVERAGE_OPTS)

coverage-xml: test-coverage
	$(COVERAGE) xml $(COVERAGE_OPTS)

migrate:
	env/bin/python3 manage.py makemigrations $(PROJECT)
	env/bin/python3 manage.py migrate $(PROJECT)

run:
	env/bin/python3 manage.py runserver 0.0.0.0:8000
