#!/usr/bin/env python
from pathlib import Path
import re

EMACS_BOOKMARKS_LOCATION = Path.home() / Path(".bookmarks.org")
BOOKMARK_FILE_LOCATION = Path.home() / Path("firefox-bookmarks.html")

BOOKMARK_FILE_START = """
<!DOCTYPE NETSCAPE-Bookmark-file-1>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<meta http-equiv="Content-Security-Policy"
      content="default-src 'self'; script-src 'none'; img-src data: *; object-src 'none'"></meta>
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks Menu</H1>
<DL><p>
"""

BOOKMARK_FILE_END = """
</DL><p>
</DL>
"""

if not EMACS_BOOKMARKS_LOCATION.is_file():
    print(f"{EMACS_BOOKMARKS_LOCATION} does not exist")
    exit()

with open(EMACS_BOOKMARKS_LOCATION, "r") as f:
    emacs_bookmark_content = f.read()

bookmarks_string = ""

for line in emacs_bookmark_content.splitlines():
    splitted_string = re.sub(r"(\* \[\[)|(]\[)|(]])|:\w.*", r" ", line)[1:].strip().split(" ", 1)
    bookmarks_string += f'<DT><A HREF="{splitted_string[0]}">{splitted_string[1]}</A>\n'

with open(BOOKMARK_FILE_LOCATION, "w") as f:
    f.write(BOOKMARK_FILE_START)
    f.write(bookmarks_string)
    f.write(BOOKMARK_FILE_END)
