import json as js
import numpy as np

n_sites = 5

labels = ["site_id","latitude","longitude","composition"]
discreteness = [0,0,1] # 0 for continuous, 1 for discrete

intRanges = np.array([[16,2],[82,2]])
strRanges = [
    np.array(["stony","iron","stony-iron"])
    ]

rng = np.random.default_rng()
###

n_labels = len(labels)-1

data = np.zeros(shape=(n_sites,n_labels),dtype=object)

iR = 0
sR = 0
for j in range(n_labels):
    if discreteness[j]  == 1:
        item = strRanges[sR]
        data[:,j] = item[rng.integers(0,high=len(item),size=n_sites)]
        sR+=1
    else:
        data[:,j] = rng.random(n_sites)*intRanges[iR,1] + intRanges[iR,0]
        iR+=1

sites = []
for i in range(n_sites):
    site = {labels[0]: i}
    for j in range(n_labels):
        site[labels[j+1]] = data[i,j]
    sites.append(site) 
data = {"sites": sites}

with open('sites.json','w') as f:
    js.dump(data,f,indent=2)