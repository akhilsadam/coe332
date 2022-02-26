FROM ubuntu:20.04
RUN apt-get update && apt-get upgrade -y
RUN apt install zlib1g
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install numpy pytest matplotlib pytest
ADD code/ /code/
ADD data/ /data/
RUN chmod +rx /code/land.py
ENV PATH "/code:$PATH"