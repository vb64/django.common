.PHONY: all clean flake8 tests

ifeq ($(OS),Windows_NT)
include windows.mk
else
include linux.mk
endif

all: flake8

flake8:
	@$(PYTHON) -m flake8 --max-line-length=110 source
	@$(PYTHON) -m flake8 --max-line-length=110 tests

# sudo find / | grep google-cloud-sdk
# make tests >log_file 2>&1
tests: flake8
	@make -C tests

clean:
	make -C source clean

setup:
	@$(PYTHON) -m pip install -r requirements.txt
	@$(PYTHON) -m pip install coverage
