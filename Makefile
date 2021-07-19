#
# Overall makefile for Getting Unstuck. 
#
# Performs any compilation steps required to build the site.
#

.PHONY: all
all: scss

.PHONY: scss
scss:
	$(MAKE) -C scss

.PHONY: clean
clean: scss-clean

.PHONY: scss-clean
scss-clean:
	$(MAKE) -C scss clean
