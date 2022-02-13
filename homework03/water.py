#! /usr/bin/env python3
# taking a slightly different approach in that I plan to auto-download data...

import os
import json as js
import numpy as np

name = "turbidity_data"
ext = ".json"
datafile=name+ext
sep=" "

def read(url:str)->dict:
    """Get JSON data from url.

    Args:
        url (str): data location.

    Returns:
        dict: stored data in JSON file.
    """
    if not os.path.exists(datafile):
        os.system("wget"+sep+datafile+sep+url)
    
    with open(datafile,'r') as file:
        data = js.load(file)
    
    return data

def turbidity(a0:float,I90:float)->float:
    """Calculates turbidity.

    Args:
        a0 (float): calibration constant.
        I90 (float): 90-degree current

    Returns:
        float: turbidity in NTU units
    """
    return a0*I90

def time(T:float,Ts:float,d:float)->float:
    """Calculates time to safe water.

    Args:
        T (float): current turbidity.
        Ts (float): threshold turbidity.
        d (float): decay constant.

    Returns:
        float: time to safe water.
    """
    return np.log(Ts/T) / np.log(1-d)

def core():
    data = sorted(read("https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json")[name], key=lambda p: p["datetime"], reverse=True)

if __name__ == '__main__':
    core()
