.PHONY: all clean

ifeq ($(OS),Windows_NT)
include ../windows.mk
else
include ../linux.mk
endif

all:

clean:
	-$(DEL) *.pyc >nul
