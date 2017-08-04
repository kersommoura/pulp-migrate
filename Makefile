CPU_COUNT=$(shell python3 -c "from multiprocessing import cpu_count; print(cpu_count())")

help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo "  help           to show this message"
	@echo "  lint           to run all linters"
	@echo "  lint-flake8    to run the flake8 linter"
	@echo "  lint-pylint    to run the pylint linter"

lint-pylint:
	pylint -j $(CPU_COUNT) --reports=n --disable=I \
		pulp_migrate/constants.py \
		pulp_migrate/populate.py \
		pulp_migrate/test_restore.py \
		pulp_migrate/utils.py \
		pulp_migrate/clean.py

lint: lint-flake8 lint-pylint

.PHONY: help lint-flake8 lint-pylint lint
