#!/usr/bin/bash

pelican content -o output -s pelicanconf.py
ghp-import output -b gh-pages
git push git@github.com:lociii/lociii.github.io.git gh-pages:master
