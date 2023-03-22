#!/bin/bash

args=("$@") 
len=${#args[@]} 
result=""

for (( i=$len-1; i>=0; i-- )) 
do
	result+="${args[i]} "
done

echo "$result"
