.PHONY: tests verbose

ifeq ($(OS),Windows_NT)
include ../windows.mk
else
include ../linux.mk
endif

PROJECT = ../source
COVERAGE = $(PYTHON) -m coverage

tests:
	@$(PYTHON) tests.py $(PROJECT)

verbose:
	@$(PYTHON) tests.py $(PROJECT) verbose

coverage:
	@$(COVERAGE) run tests.py $(PROJECT)

report:
	@$(COVERAGE) report --skip-covered

html:
	@$(COVERAGE) html --skip-covered
