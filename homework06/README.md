<!-- ⚠️ This README has been generated from the file(s) "blueprint.md" ⚠️--><h1 align="center">flask-cube-redis</h1>
<p align="center">
  <b>An containerized Flask webserver to read and update a Redis container, through Kubernetes. HW06 for COE332.</b></br>
  <sub><sub>
</p>

<br />

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/cloudy.png)](#implementation)

#  Implementation

We use the `homework05` docker image as is, so the necessary items for that are included in the `./homework05` folder.
This repo is only designed to be run on the TACC COE-332 Kubernetes system, and any deviations from the following procedure may not behave as expected.


[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/cloudy.png)](#files)

##  Files

- `/deployment/` - contains all the kubernetes deployment files:

 - `data-redis-volume.yml` - makes the persistent volume
 - `deployment-debug.yml` - for debugging the deployments
 - `deployment-flask.yml` - deployment for flask container
 - `deployment-redis.yml` - deployment for redis container
 - `service-flask.yml` - service for flask container
 - `service-redis.yml` - service for redis container

- `/homework05/` - contains everything necessary for the `flask-redis` docker image. Note this is completely identical to the `homework05` submission --- nothing has changed.

- `Makefile` - a makefile for ease of use
- `repl.sh` - a sh script to automatically query the Redis service IP and input to the Flask deployment.

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/cloudy.png)](#input-data)

##  Input Data

- The application queries data from the following location: <a href="https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json">https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json</a>, which looks as follows:

```
{
  "meteorite_landings": [
    {
      "name": "Gerald",
      "id": "10001",
      "recclass": "H4",
      "mass (g)": "5754",
      "reclat": "-75.6691",
      "reclong": "60.6936",
      "GeoLocation": "(-75.6691, 60.6936)"
    },
    {
      "name": "Dominique",
      "id": "10002",
      "recclass": "L6",
      "mass (g)": "1701",
      "reclat": "-9.4378",
      "reclong": "49.5751",
      "GeoLocation": "(-9.4378, 49.5751)"
    },
    {
      "name": "Malinda",
      "id": "10003",
      "recclass": "CI1",
      "mass (g)": "3482",
      "reclat": "35.3692",
      "reclong": "61.4206",
      "GeoLocation": "(35.3692, 61.4206)"
    },
    {
      "name": "Mary",
      "id": "10004",
      "recclass": "L5",
      "mass (g)": "5339",
      "reclat": "71.2364",
      "reclong": "-21.9294",
      "GeoLocation": "(71.2364, -21.9294)"
    },
    ...
  ]
}
```

This data is stored in the Redis deployment and updated / read via the Flask deployment.


[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/cloudy.png)](#installation--usage)

#  Installation & Usage

There is really only one way to run this project. Please replace `as_tacc` with your username in all following sshes.

First, log in to ISP02, and then the Kubernetes Cloud:
`ssh as_tacc@isp02.tacc.utexas.edu`
`ssh as_tacc@coe332-k8s.tacc.cloud`

Next, clone this GitHub repository and `cd` into this folder:
`git clone <the cloning url for this repository>`
`cd coe332/homework06/`

Now we can deploy the Flask and Redis deployments. The Makefile will do this for us:
`make iterate`

To see that the deployments, services, and pods are up & running, do the following:
`kubectl get pods`
`kubectl get deployments`
`kubectl get services`

We can also inspect the services to make sure the correct number of pods exist (2 for Flask, 1 for Redis):
`kubectl describe service flask-cube-redis-flask-service` (will have two addresses under endpoints)
`kubectl describe service flask-cube-redis-redis-service` (will have one address under endpoints)

Now to test that the system is working, start by deploying the debug deployment:
`kubectl apply -f deployment/deployment-debug.yml`
Find the IP address of the Flask service, and the complete debug pod name with the `kubectl get services` command and the `kubectl get pods` command.
Now `exec` into the debug deployment terminal with the following command, replacing `<py-debug-deployment>` with the complete pod name:
`kubectl exec -it <py-debug-deployment> -- /bin/bash`
We can now query the data routes listed in the API reference below by running the given curl commands (of course, replacing the `<url>` with the IP address of the Flask service).


The Redis server is also tested in this manner, so there is no need to specifically interact with the Redis server. We will not be providing commands for that here.

To test persistence, simply delete the Redis pod via `kubectl delete pod <podname>`, where `<podname>` is the name of the `flask-cube-redis-redis` pod that can be found with the `kubectl get pods` command.

Regeneration of pods can also be tested in a similar manner.

<details>
<summary> Complete API Reference </summary>


[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/cloudy.png)](#rest-api)

##  REST API:

### ENDPOINT (POST) : `/data`
 - Description: Update Redis database with Meteorite Landings data.
 - Parameters: 
   -  N/A
 - Responses: 
   -  A `201` response will : Update the database and return a success message.

 - Example: `curl -X POST <url>:5000/data -H "accept: application/json"`
 - Example Output:
```
Successful Load!
```

 ### ENDPOINT (GET): `/data`
 - Description: Get Meteorite Landings (ML) data from Redis database.
 - Parameters: 
   -  (optional) Start query parameter to index the ML list.
 - Responses: 
   -  A `200` response will : Return the indexed list as JSON.

 - Example: `curl -X GET <url>:5000/data -H "accept: application/json"`
 - Example Output:
```
[{"GeoLocation":"(74.4431, -65.2342)","id":"10010","mass (g)":"3644","name":"Helga","recclass":"L5","reclat":"74.4431","reclong":"-65.2342"},{"GeoLocation":"(-46.4123, 58.0161)","id":"10099","mass (g)":"7317","name":"John","recclass":"H6","reclat":"-46.4123","reclong":"58.0161"},{"GeoLocation":"(-12.9202, 33.6740)","id":"10171","mass (g)":"7419","name":"Marisol","recclass":"CV3","reclat":"-12.9202","reclong":"33.6740"},{"GeoLocation":"(84.8000, 14.6012)","id":"10222",
......
]
```

</details>


[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/cloudy.png)](#contributors)

##  Contributors
	

| [Akhil Sadam](https://github.com/akhilsadam) |
|:----------------------------------------------:|



[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/cloudy.png)](#license)

##  License
	
Licensed under [MIT](https://opensource.org/licenses/MIT).