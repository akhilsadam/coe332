#!/bin/bash
firstString=$(<deployment-flask.yml)
secondString=$(echo $(kubectl get services flask-cube-redis-redis-service --output=jsonpath="{.spec.clusterIP}") | tr -d '"')
echo $secondString
repline=${firstString/ip_address/"$secondString"}
echo "#repline"   
echo $repline > deployment-flask.yml