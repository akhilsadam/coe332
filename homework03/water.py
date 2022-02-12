#! /usr/bin/env python3
# taking a slightly different approach in that I plan to auto-download data...

import os
import json as js
import numpy as np

datafile="turbidity_data.json"
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


def core():
    data = read("https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json")

if __name__ == '__main__':
    core()
