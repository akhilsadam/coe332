#!/bin/bash
firstString=$(<deployment.yml)
secondString=$(kubectl get services flask-cube-redis-redis-service --output=jsonpath="{.spec.clusterIP}")
echo $secondString
echo "${firstString/ip_address/"$secondString"}"   