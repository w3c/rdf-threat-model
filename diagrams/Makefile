.PHONY: all
all: diagram1.svg diagram2.svg diagram3.svg diagram4.svg

.PRECIOUS: diagram1.dot diagram2.dot diagram3.dot diagram4.dot

%.svg: %.dot shapes/*.svg Makefile
	dot "$<" -Tsvg | sed 's/xMinYMin meet/none/' > "$@"
	# the sed above replaces 'preserveAspectRatio' on embedded images,
	# to force them to be stretched to the shape of the node

diagram%.dot: source.dot
	python make_subgraph.py <"$<" "$@" >"$@"


.PHONY: clean
clean:
	rm -f diagram*.svg diagram*.dot
