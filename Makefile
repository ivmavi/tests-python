#    Copyright 2022 name of copyright ivmavi

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

VENV ?= .venv
PYTHON ?= python3
PIP ?= pip3

.SILENT:

.PHONY: help
help:
	@echo "Targets:"
	@echo ""
	@grep '^## @help' Makefile|cut -d ":" -f 2-3|( (sort|column -s ":" -t) || (sort|tr ":" "\t") || (tr ":" "\t"))

## @help:virtualenv:Create a Python virtual environment.
.PHONY: virtualenv
virtualenv:
	$(PYTHON) --version
	test -d $(VENV) || $(PYTHON) -m venv $(VENV);\
	source $(VENV)/bin/activate;\
	$(PIP) install -q -r requirements.txt;

## @help:test:Run the test.
.PHONY: test
test: virtualenv
	source $(VENV)/bin/activate;\
	$(PYTHON) -m pytest --junitxml $(CURDIR)/junit-test_suite.xml \
		tests/test_suite.py;

## @precomit:pre-commit:Run precommit hooks.
lint: virtualenv
	source $(VENV)/bin/activate;\
	pre-commit run; \
	mypy src/test_python; \
	mypy mypy tests;

## @help:clean:Remove Python file artifacts.
.PHONY: clean
clean:
	@echo "+ $@"
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete
	@find . -name '*~' -delete
	-@rm -fr *.egg-info build dist $(VENV) bin .tox .mypy_cache temp junit-*.xml .pytest_cache

