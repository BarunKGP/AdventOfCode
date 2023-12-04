# Advent of Code
[Advent of Code](https://adventofcode.com/) is an annual coding challenge held every December following the Advent calendar. Each day a problem is released in two parts. The second part is revealed when you complete the first. Depending on how you implemented the first part, you might be in for a world of pain when solving the second part, or it might be a breeze. The two parts are usually closely related problems. There is a leaderboard and the fastest solutions wins 100 points, with the awarded points decreasing by one for each successive submission, until the fastest 100 submissions have been awarded.


Advent of Code is an outlet for me to experiment with different solutions without necessarily caring about speed or optimizations. Sometimes, it is rather exciting to just dive into problems and solve them. Sometimes it is an opportunity to try new approaches and languages. All in all, it is great fun, and a good learning experience. This repo contains my solutions to these problems for each year, starting in 2023.

## Helpful files
There are a few helper files here that work well as starter scripts for me. You are free to fork this repo and use these scripts for your own Advent of Code journey if you find them helpful :)

- `init_aoc.sh` intializes an `aoc{day}` directory with some Python boilerplate for each day of Advent of Code
- `aoctemplate.py` is my main template file where I code up my solutions. `init_aoc.sh` copies this to the current day's directory and renames it accordingly
- `config.py` contains some config helpers to set up boilerplate in projects

Each `aoc{day}` repository contains my code for that day's problem. They usually follow the same directory structure and most of them are created using the scripts.

## Running helper scripts
1. Clone the repo using `git clone https://github.com/BarunKGP/AdventOfCode.git`
2. cd into the cloned directory `cd ./AdventOfCode`
3. Give execution privileges to `init_aoc.sh` using `chmod +x init_aoc.sh`
4. You can now create a new directory for a particular day that is a self-contained module using `./init_aoc.sh -d [DAY]`.

For instance, running `./init_aoc.sh 13` would create the directory `aoc13` with the following files:
```
aoc13
  __init__.py
  aoc13.py
  aoc13data.txt
  aoc13example.txt
```
I use `aoc13data.txt` to store the puzzle input for the day and `aoc13example.txt` to store the example input given in the problem. The solution lives in `aoc13.py`.

You will have to copy the relevant puzzle inputs to the data files when they release. This is simple enough for me that I don't need to automate it (yet!) because I usually copy in the data as soon as I start the problem.

The scripts also have an additional `--example` or `-e` flag which when passed loads in the data from `aoc13example.txt` instead of the usual `aoc13data.txt`. This is useful when debugging or developing solutions that you might need to test on the example inputs.




**Happy Adventing** 🎄🎅✨🎉
