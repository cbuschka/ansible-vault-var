TOP_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
SHELL := /bin/bash

init:
	@if [ -z "$(shell pipenv --version 1>/dev/null 2>&1)" ]; then \
		pip install pipenv; \
	else \
		echo "pipenv is available, good."; \
	fi

install_deps:	init
	@echo "Installing deps..."; \
	pipenv install --dev -r requirements.txt -r requirements-dev.txt


tests:	init
	@echo "Running tests..."; \
	pipenv run python3 -B -m unittest discover -s ${TOP_DIR}/tests/ -p '*_test.py'

run:	init
	@echo "Running installed_packages_diff..."; \
	pipenv run python3 -B -m installed_packages_diff ${TOP_DIR}/config.yaml

dist:   clean install_deps tests
	@echo "Bulding dist..."; \
	pipenv run python3 ${TOP_DIR}/setup.py sdist bdist_wheel

clean:
	rm -rf ${TOP_DIR}/dist/ ${TOP_DIR}/build/ *.egg-info/

upload: dist
	@echo "Uploading dist..."; \
	pipenv run twine upload dist/*
