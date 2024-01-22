FILE = plot.py
.PHONY: tags
tags:
	ctags -R . --languages=python

.PHONY: tags-stdout
tags-stdout:
	@printf "=== $(FILE) ===\n"
	@ctags -x $(FILE) --languages=python

# Test plot.py with doctest: ;t<Space> (but there are no doctests in it yet...)
# Test mjg_plot by sourcing it: ;so (it uses unittest)
# Or uncomment everything below to test everything with doctest.
.PHONY: tests
tests:
	python -m doctest mjg_pygame.py
	@# python -m doctest mjg_plot.py
	@# python -m doctest plot.py
