# HW 02

This is a JSON file I/O test program.
We calculate 5 example meteorite landing sites in Syrtis Major, Mars, and measure the time for a naive path between the sites.

- .gitignore	: ignores any produced .json files
- sites.py	: creates a JSON file called sites.json containing a dictionary with one key, “sites”, whose value is a list of 5 dictionaries for each of the sites.
  - Each site dictionary stores latitude, longitude, meteorite composition
  - latitude is between `16.0 - 18.0 degrees North`
  - longitude is between `82.0 - 84.0 degrees East`
  - meteorite composition is one of the following types `["stony", "iron", "stony-iron"]`
- visit.py	: reads the produced JSON file (sites.json) and prints to screen descriptive path info, assuming the following:
  - initial latitude / longitude is `{16.0, 82.0}`
  - the five sites are visited in the order of the list index
  - vehicle speed is `10 km per hour`
  - Mars is a sphere with radius = `3389.5 km`, so the great-circle algorithm is an appropriate distance metric
  - meteorite sample time is as follows: stony meteorites take `1 hour` to sample, iron meteorites take `2 hours` to sample, and stony-iron meteorites take `3 hours` to sample.
