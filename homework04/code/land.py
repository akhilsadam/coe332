#!/usr/bin/env python3
import json
import sys
from typing import List
import logging
import socket
import numpy as np

format_str=f'[%(asctime)s {socket.gethostname()}] %(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.WARNING, format=format_str)


def average(a_list_of_dicts: List[dict], a_key_string: str) -> float:
    """
    Iterates through a list of dictionaries, pulling out values associated with
    a given key. Returns the average of those values.

    Args:
        a_list_of_dicts (list): A list of dictionaries, each dict should have the
                                same set of keys.
        a_key_string (string): A key that appears in each dictionary associated
                               with the desired value (will enforce float type).

    Returns:
        result (float): Average value.
    """
    if not a_list_of_dicts:
        logging.error('a list of dicts is empty')
    total_mass = 0.
    for item in a_list_of_dicts:
        total_mass += float(item[a_key_string])
    return(total_mass / len(a_list_of_dicts) )


def loc(latitude: float, longitude: float) -> str:
    """
    Given latitude and longitude in decimal notation, returns which hemispheres
    those coordinates land in.

    Args:
        latitude (float): Latitude in decimal notation.
        longitude (float): Longitude in decimal notation.

    Returns:
        location (string): Short string listing two hemispheres.
    """
    if latitude == 0 or longitude == 0:
        raise(ValueError)
    location = 'Northern' if (latitude > 0) else 'Southern'
    location = f'{location} & Eastern' if (longitude > 0) else f'{location} & Western'
    return(location)


def count(a_list_of_dicts: List[dict], a_key_string: str) -> dict:
    """
    Iterates through a list of dictionaries, and pulls out the value associated
    with a given key. Counts the number of times each value occurs in the list of
    dictionaries and returns the result.

    Args:
        a_list_of_dicts (list): A list of dictionaries, each dict should have the
                                same set of keys.
        a_key_string (string): A key that appears in each dictionary associated
                               with the desired value.

    Returns:
        classes_observed (dict): Dictionary of class counts.

    """
    classes_observed = {}
    for item in a_list_of_dicts:
        if item[a_key_string] in classes_observed:
            classes_observed[item[a_key_string]] += 1
        else:
            classes_observed[item[a_key_string]] = 1
    return(classes_observed)


def main():

    with open(sys.argv[1], 'r') as f:
        ml_data = json.load(f)
    
    name = 'meteorite_landings'
    hemiL =['Northern & Eastern','Northern & Western','Southern & Eastern','Southern & Western']

    logging.debug(f'DATATYPE:{type(ml_data)}')

    hemi = np.array([loc(float(row['reclat']), float(row['reclong'])) for row in ml_data[name]])
    types = count(ml_data[name], 'recclass')

    print(f"Summary for {len(ml_data[name])} meteors:")
    print(f" - Average meteor mass = {average(ml_data[name], 'mass (g)')}g.")
    print(' - Hemisphere Distribution:')
    
    for h in hemiL:
        print(f'\t{h}: {np.count_nonzero(h == hemi)} meteors.')

    print(' - Type Distribution:')
    
    for tp in types.keys():
        adj = '\t' if len(tp) < 8 else ''
        print(f'\t{tp}:{adj}\t{types[tp]} meteors.')


if __name__ == '__main__':
    main()


