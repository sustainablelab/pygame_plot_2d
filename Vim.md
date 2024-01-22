# Vim

Remember to activate venv before launching session

```
(pydev) $ vim -S ~/temperature-python-gui.vim
```

* `;so`
  * run `plot.py` (opens Game window)
* `;t<Space>`
  * run unit tests
  * Runs Makefile recipe "tests" in Vim terminal at bottom of screen
* `;tg<Space>`
  * make tags
  * Runs Makefile recipe "tags"
* `:tag ` and tab-complete tag names
* `;ts`
  * opens Vim Quickfix window with tags, then, from Quickfix window, `;w]` with cursor on tag to jump to that part of code
  * Prints tags in Quickfix window
    * Runs Makefile recipe "tags-stdout" which prints tags to stdout
    * Tags are displayed in Quickfix window
