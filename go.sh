#!/bin/bash
#
# Shortcut to update things and store in git.  Fragile.
#

./make_book.py && git add sections/* > /dev/null && git commit -m "Updated" -a > /dev/null && git push -u origin master > /dev/null

