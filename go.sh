#!/bin/bash
#
# Shortcut to update things and store in git.  Fragile.
#

./make_book.py && git add sections/* && git commit -m "Updated" -a && git push -u origin master

