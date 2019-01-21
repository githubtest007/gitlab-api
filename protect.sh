#!/bin/bash

git_id=$1
branch=$2
git_url="https://192.168.2.49"
header="PRIVATE-TOKEN":""

#echo "curl -k --request POST --header ${header} ${git_url}/api/v4/projects/${git_id}/protected_branches?name=${branch}&push_access_level=30&merge_access_level=30"
curl -k --request POST --header ${header} "${git_url}/api/v4/projects/${git_id}/protected_branches?name=${branch}&push_access_level=30&merge_access_level=30"
