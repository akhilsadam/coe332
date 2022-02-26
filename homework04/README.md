# HW 04 Containerization

This is a Docker containerization test program, where we containerize the following project.

> ## Metorite Landing Summary Statistics
> We calculate summary statistics for meteorite landings on Mars, from a json datafile describing the landings.

## Files
- .gitignore        : ignores any temporary files
- code/land.py      : console prints summary statistics for the meteorite landings, given a json datafile.
- code/test_land.py	: tests the code/land.py file via pytest.
- data/data.json    : example meteorite landing data
- Dockerfile        : a docker instruction set to help build a docker container for the program
- Makefile          : a makefile to automate the clean / build / run / push commands for the docker container

## Input Data
- The input datafile should be of similar form to the example datafile `data/data.json` provided (below for reference).\
![](data/data.json?raw=true)

## Installation & Usage

<details open>
<summary>Docker Container</summary>



</details>

<details open>
<summary>From Source</summary>



</details>


This can be run via the following terminal commands:

Linux	: `python3 sites.py; python3 visit.py`

Windows	: `python sites.py; python visit.py`

Please note that source builds only support Python3 on Ubuntu, so ymmv for other systems.