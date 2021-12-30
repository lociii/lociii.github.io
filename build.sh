#!/usr/bin/bash

pelican content -o output -s pelicanconf.py
pelican --listen --port 9999