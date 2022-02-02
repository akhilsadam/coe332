import json as js
import numpy as np
import math

with open('sites.json', 'r') as f:
    sites = js.load(f)["sites"]

n_sites = len(sites)

current_loc = [16.0,82.0]
speed =  10
mars_radius = 3389.5
units = ["km","hr"]
sampletime = {"stony":1,"iron":2,"stony-iron":3}

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

etime = 0

for i in range(n_sites):
    site = sites[i]
    loc = [site["latitude"],site["longitude"]]
    dist = calc_gcd(current_loc[0],current_loc[1], loc[0], loc[1])
    ttime = dist/speed
    stime = sampletime[site["composition"]]
    etime += ttime + stime
    print("leg = ",i, ", travel time = ",ttime," ",units[1],", sample time = ",stime," ",units[1])
    current_loc = loc

print("# of Legs = ",n_sites,", elapsed time = ",etime," ",units[1])


