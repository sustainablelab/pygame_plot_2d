# About

This is a simple utility to plot 2D data. The motivation for this is to have a "live" plotting program that can take data from an embedded system connected over USB.

# Status

Source `plot.py`. This opens a black window with some debug text and a 2d grid.

* `N` : increase number of grid lines
* `Shift+N` : decrease number of grid lines

Set window size in `plot.py` using `OS_WIN_SCALE`.

# Dependencies

Install pygame to a virtual environment. Activate the virtual environment for development and for usage.

# Design

Use pygame.

Keep the pygame boilerplate in `mjg_pygame.py` in class `PGG` (PyGame Globals). Inherit `PGG` in the main application `plot.py` to make child class `GUI` with application-specific stuff.

The `plot.py` script in this repo is meant to be an example application. I'm trying to keep the code in `plot.py` minimal and put most of the code into unit tested modules.

Modules start with `mjg_`. The main script does not have the `mjg_` prefix.

# Unit tests

Unit test with both `unittest.Testcase` and with `doctest`. Use `unittest` for traditional assert-style unit tests. Use `doctest` when traditional assert-style unit tests are too much work. Use `doctest` to keep the docstrings in sync with the code.

I don't unit test `mjg_pygame.py` because I don't know how and it's just glue anyway. This module is not going anywhere.

The other modules are unit-tested but they are subject to change a lot as I discover how this project wants to come together. For now, the other modules are `mjg_calc.py` and `mjg_plot.py`.
