SVGS=$(shell ls *.dot | sed 's/dot$$/svg/')

.PHONY: all
all: ${SVGS}

%.svg: %.dot Makefile
	sfdp "$<" -Tsvg -o "$@"

.PHONY: clean
clean:
	rm -r ${SVGS}
