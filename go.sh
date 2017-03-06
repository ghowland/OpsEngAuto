#!/bin/bash
#
# Shortcut to update things and store in git.  Fragile.
#

#./make_book.py

./make_book.py && git add __toc_backups/* > /dev/null && git add sections/* > /dev/null && git commit -m "Updated" -a > /dev/null && git push -u origin master > /dev/null

# Make the book with Sphinx

./make_sphinx.sh

