FILE = plot.py
.PHONY: tags
tags:
	ctags $(FILE) --languages=python

.PHONY: list-tags
list-tags:
	@printf "=== $(FILE) ===\n"
	@ctags -x $(FILE) --languages=python

.PHONY: test
test:
	python -m doctest mjg_plot.py
