#!/usr/bin/env python
from pathlib import Path
import re

EMACS_BOOKMARKS_LOCATION = Path.home() / Path(".bookmarks.org")
QUTEBROWSER_QUICKMARKS_LOCATION = Path.home() / Path(".config/qutebrowser/quickmarks")

if not EMACS_BOOKMARKS_LOCATION.is_file():
    print(f"{EMACS_BOOKMARKS_LOCATION} does not exist")
    exit()

if not QUTEBROWSER_QUICKMARKS_LOCATION.is_file():
    print(f"{QUTEBROWSER_QUICKMARKS_LOCATION} does not exist")
    exit()

with open(EMACS_BOOKMARKS_LOCATION, "r") as f:
    emacs_bookmark_content = f.read()

qutebrowser_quickmarks_string = ""

for line in emacs_bookmark_content.splitlines():
    splitted_string = re.sub(r"(\* \[\[)|(]\[)|(]])|:\w.*", r" ", line)[1:].strip().split(" ", 1)
    # splitted_string[0] = url
    # splitted_string[1] = name
    qutebrowser_quickmarks_string += f"{splitted_string[1]} {splitted_string[0]}\n"

with open(QUTEBROWSER_QUICKMARKS_LOCATION, "w") as f:
    f.write(qutebrowser_quickmarks_string)
