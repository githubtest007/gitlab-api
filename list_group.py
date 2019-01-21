#!/usr/bin/bash

import requests
import json
import os
import warnings
warnings.filterwarnings('ignore')

gitlab_url = "https://192.168.2.49"
gitlab_ssh = "git@192.168.2.49:"
headers = {"PRIVATE-TOKEN":""}   #duanyuying api
params = {"per_page":"100"}


#gitlab_url = "http://192.168.1.85"
#headers = {"PRIVATE-TOKEN":""}   #root api

#curl -k --header "PRIVATE-TOKEN: " https://192.168.2.49/api/v4/groups?

url = gitlab_url + '/api/v4/groups?'
response = requests.get(url,headers=headers,params=params,verify=False)
#print(response.text)
data = json.loads(response.text)
#print data
for i in range(0,len(data)):
    print(data[i]['full_path'],data[i]['id'])
