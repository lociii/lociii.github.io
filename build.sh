#!/usr/bin/bash

pelican content -o output -s pelicanconf.py
pelican --autoreload --listen --port 9999