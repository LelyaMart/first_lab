#!/bin/bash

args=("$@") 
len=${#args[@]} 
result=""
i=$((len-1))

while [ $i -ge 0 ] 
do
	result+="${args[i]} "
	i=$((i-1)) 
done

echo "$result"
