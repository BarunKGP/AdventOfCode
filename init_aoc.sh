#!/bin/bash

mkdir -p aoc${1}
cp aoctemplate.py aoc${1}/aoc${1}.py
touch aoc${1}/aoc${1}data.txt aoc${1}/aoc${1}example.txt aoc${1}/__init__.py

echo "Created files in ./aoc${1}\nHappy Adventing...."
