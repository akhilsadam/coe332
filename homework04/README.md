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
- The input datafile should be of similar form to the example datafile `data/data.json` provided.

<details open>
<summary>data.json (HEAD)</summary>

```
{
 "meteorite_landings": [
   {
     "name": "Ruiz",
     "id": "10001",
     "recclass": "L5",
     "mass (g)": "21",
     "reclat": "50.775",
     "reclong": "6.08333",
     "GeoLocation": "(50.775, 6.08333)"
   },
   {
     "name": "Beeler",
     "id": "10002",
     "recclass": "H6",
     "mass (g)": "720",
     "reclat": "56.18333",
     "reclong": "10.23333",
     "GeoLocation": "(56.18333, 10.23333)"
   },
  ]
}
```

</details>

## Installation & Usage

<details>
<summary>Docker Container</summary>

### Install
- Note `docker run` will also pull the necessary image.
- Install Docker:
 - `apt-get install docker` (if you are on an Ubuntu machine)
### Run 
- (with data `<pathtodatafile.json>`) (use a path to the file `data/data.json` to see example output)
 - `docker run --rm -v \${PWD}:/data ${NAME}/ml_data_analysis:hw04 land.py <pathtodatafile.json>`

</details>

<details>
<summary>From Source</summary>

- Please note that source builds only support Python3 on Ubuntu 20.04, and are written in that fashion. Your mileage may vary for other systems.
### Install
- First, install all dependencies:
```
apt-get install zlib1g python3 python3-pip -y
pip3 install numpy pytest matplotlib
```
- Then clone this repository and initialize script:
```
git clone https://github.com/akhilsadam/coe332.git 
cd coe332/homework04/
chmod +rx code/land.py
```
### Run
- Tester
 - Any tester output without an `AssertionError` is valid.
```
pytest
```
- Run (with data `<pathtodatafile.json>`) (use `data/data.json` to see example output)
```
code/land.py <pathtodatafile.json>
```
</details>

## Example Output

<details open>
<summary>output for data.json file</summary>

```
Summary for 30 meteors:
 - Average meteor mass = 83857.3g.
 - Hemisphere Distribution:
        Northern & Eastern: 21 meteors.
        Northern & Western: 6 meteors.
        Southern & Eastern: 0 meteors.
        Southern & Western: 3 meteors.
 - Type Distribution:
        L5:             1 meteors.
        H6:             1 meteors.
        EH4:            2 meteors.
        Acapulcoite:    1 meteors.
        L6:             6 meteors.
        LL3-6:          1 meteors.
        H5:             3 meteors.
        L:              2 meteors.
        Diogenite-pm:   1 meteors.
        Stone-uncl:     1 meteors.
        H4:             2 meteors.
        H:              1 meteors.
        Iron-IVA:       1 meteors.
        CR2-an:         1 meteors.
        LL5:            2 meteors.
        CI1:            1 meteors.
        L/LL4:          1 meteors.
        Eucrite-mmict:  1 meteors.
        CV3:            1 meteors.
```

</details>

