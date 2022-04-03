<!-- ⚠️ This README has been generated from the file(s) "blueprint.md" ⚠️--><h1 align="center">flask-redis</h1>
<p align="center">
  <b>An containerized Flask webserver designed for querying ISS sightings and positions on February 13, 2022.
Midterm project for COE332.</b></br>
  <sub><sub>
</p>

<br />



[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/cloudy.png)](#implementation)

#  Implementation

This project uses Python3 (in particular Flask), and Docker for containerization. Specific Python3 package requirements can be found <a href="https://github.com/akhilsadam/positional-iss/blob/master/requirements.txt">here</a>. R and the npm package `@appnest/readme` by Andreas Mehlsen are used for documentation, but are not part of the API and will not be documented.



A list of important files can be found below.


[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/cloudy.png)](#files)

##  Files

 - `app/`:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The application folder.
 - `doc/`:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A documentation folder.
 - `Dockerfile`:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A dockerfile for containerization.
 - `Makefile`:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A makefile for ease of compilation.
 - `requirements.txt`:&nbsp;&nbsp;&nbsp;&nbsp;The list of Python3 requirements.
 - `core.py`:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The main Python file.

### The App/ Directory

- `api/`:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contains API route definitions in Python.
- `routes.py`:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Collects the API route definitions.






[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/cloudy.png)](#input-data)

##  Input Data

- The application queries data from the National Aeronautics and Space Administration (NASA) public website, in particular ISS positional information via the <a href="https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_OEM/ISS.OEM_J2K_EPH.xml">Public Distribution file</a> and regional sighting data for the Midwest via the <a href="https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_sightings/XMLsightingData_citiesUSA05.xml">XMLsightingData_citiesUSA05</a> file.


{{ load:doc/inputG.md }}


[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/cloudy.png)](#installation--usage)

#  Installation & Usage

A user can build this project from source, or use the provided Docker container on DockerHub.  
A Docker installation is required for source builds, as we build and run a Docker image.




The following commands are all terminal commands, and are expected to run on a Ubuntu 20.04 machine with Python3, and are written in that fashion. Mileage may vary for other systems. We will describe the Docker installation first.   

### From Docker:

#### Install

To install the Docker container, first install Docker.  

  - `apt-get install docker` (if using an Ubuntu machine, else get Docker from <a href="https://www.docker.com/">docker.com</a>.)  
  
Next install the containers.  

  - `docker pull akhilsadam/positional-iss:0.0.2`  

#### Run  

To test the code, please run the following in a terminal.  

  - `docker run -it --rm akhilsadam/positional-iss:0.0.2 testall.py`  


To run the code, please run the following in a terminal. The terminal should return a link, which can be viewed via a browser or with the `curl` commands documented in the API reference section.  

  - `docker run --name "positional-iss" -p 5026:5026 akhilsadam/positional-iss:0.0.2 wsgi.py`  


Now we will move to the source installation.  

### From Source:  

Since this is a Docker build, the requirements need not be installed on the server, as it will automatically be done on the Docker image.  
All commands, unless otherwise noted, are to be run in a terminal (in the home directory of the cloned repository).  

#### Build  

Again, first install Docker.  

  - `apt-get install docker` (if using an Ubuntu machine, else get Docker from <a href="https://www.docker.com/">docker.com</a>.)  
  
Next, clone the repository and change directory into the repository.  

  - `git clone git@github.com:akhilsadam/positional-iss.git`  

  - `cd positional-iss`  


Now build the image.  

  - `make build`  

#### Run  

To test the code, please run one of the following.  

  - `make test`  

  - `pytest`  


To run the code, please run the following. The terminal should return a link, which can be viewed via a browser or with the `curl` commands documented in the API reference section.  

  - `make run`  

To run a rebuild of the code, run this command instead. This command will automatically kill, rebuild, and test the code before running.  

  - `make iterate`  




[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/cloudy.png)](#usage--)

##  Usage  



As mentioned above, a browser or the `curl` utility is necessary to view output. All endpoints as mentioned in the REST API section are valid urls, and navigating to those links will return expected output as included in this document.


<details>
<summary> Complete API Reference </summary>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>


</details>

<!-- 
[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/cloudy.png)](#table-of-contents)

##  Table of Contents

* [ Implementation](#-implementation)
	* [ Files](#-files)
		* [The App/ Directory](#the-app-directory)
	* [ Input Data](#-input-data)
* [ Installation & Usage](#-installation--usage)
		* [From Docker:](#from-docker)
			* [Install](#install)
			* [Run  ](#run--)
		* [From Source:  ](#from-source--)
			* [Build  ](#build--)
			* [Run  ](#run---1)
	* [ Usage  ](#-usage--)
	* [ Contributors](#-contributors)
	* [ License](#-license) -->

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/cloudy.png)](#contributors)

##  Contributors
	

| [Akhil Sadam](https://github.com/akhilsadam) |
|:----------------------------------------------:|



[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/cloudy.png)](#license)

##  License
	
Licensed under [MIT](https://opensource.org/licenses/MIT).