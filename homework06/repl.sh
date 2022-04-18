#!/bin/bash
firstString=$(<deployment.yml)
secondString=$(echo $(kubectl get services flask-cube-redis-redis-service --output=jsonpath="{.spec.clusterIP}") | tr -d '"')
echo $secondString
echo "${firstString/ip_address/"$secondString"}"   