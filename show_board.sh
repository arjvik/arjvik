#!/bin/bash

[[ $1 == 'update' ]] && python3 update_life.py

head -n16 README.md | sed -e 's/:black\w*:  /⬛/g' -e 's/:white\w*:  /⬜/g' 
