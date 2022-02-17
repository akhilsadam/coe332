#! /usr/bin/env python3
# taking a slightly different approach in that I plan to auto-download data...

import os
import json as js
import logging as log
from typing import List
import numpy as np

name = "turbidity_data"
ext = ".json"
datafile=name+ext
sep=" "

cc = "calibration_constant"
dc = "detector_current"

THRESHOLD = 1

logger = log.getLogger(__name__)

def read(url:str) -> dict:
    """Get JSON data from url.

    Args:
        url (str): data location.

    Returns:
        dict: stored data in JSON file.
    """
    if type(url) != str:
        raise(TypeError)

    if not os.path.exists(datafile):
        os.system(f'wget{sep}{datafile}{sep}{url}')

    with open(datafile,'r') as file:
        data = js.load(file)

    return data

def turbid(a0:float,I90:float) -> float:
    """Calculates turbidity.

    Args:
        a0 (float): calibration constant.
        I90 (float): 90-degree current

    Returns:
        float: turbidity in NTU units
    """
    return a0*I90

def time(T:float,Ts:float=THRESHOLD,d:float=0.02)->np.float64:
    """Calculates time to safe water.

    Args:
        T (float): current turbidity.
        Ts (float): threshold turbidity.
        d (float): decay constant.

    Returns:
        float: time to safe water.
    """
    if d>=1 or T < 0:
        log.critical("Nonphysical Decay Constant...\nExit")
        return -1
    t = np.log(Ts/T) / np.log(1-d)
    return max(t,0.0)

def sort(d:List[dict],k:str)->list:
    """Sorts list of dictionaries by key.

    Args:
        d (List[dict]): list of dictionaries to sort.
        k (str): key to sort with.

    Returns:
        list: sorted items of dict.
    """
    if type(d) != list:
        raise(TypeError)
    return sorted(d, key=lambda p: p[k], reverse=True)

def current(d:List[dict],n:int=5)->float:
    """Calculates most-recent turbidity average.

    Args:
        d (List[dict]): turbidity data.
        n (int): moving-average block size.
    Returns:
        float: most-recent turbidity average.
    """
    if type(d) != list or type(n) != int:
        raise(TypeError)
    value = 0.0
    for e in d[:n]:
        value += turbid(e[cc],e[dc])
    return value/len(d[:n])

def core():
    data = sort(read("https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json")[name],"datetime")
    turbidity = current(data)
    print("Average turbidity based on most recent five measurements = {} NTU".format(turbidity))

    if turbidity > THRESHOLD :
        log.warning("Turbidity is above threshold for safe use")
    else:
        log.info("Turbidity is below threshold for safe use")

    print("Minimum time required to return below a safe threshold = {} hours".format(time(turbidity)))
    # note I did not add a format specifier since I rather like the extra digits (no need for significant figures here)!

if __name__ == '__main__':
    core()
