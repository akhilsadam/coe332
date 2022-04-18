#!/bin/bash
firstString=$(<deployment.yml)
secondString=$(kubectl get services)
echo $secondString
echo "${firstString/ip_address/"$secondString"}"   