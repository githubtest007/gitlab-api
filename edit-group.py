#!/usr/bin/python
import requests

gitlab_url = "https://192.168.2.49"
headers = {"PRIVATE-TOKEN":""}   #duanyuying api

#gitlab_url = "http://192.168.1.85"
#headers = {"PRIVATE-TOKEN":""}   #root api

#curl -k --request POST --header "PRIVATE-TOKEN: "  --data "name=Test22&path=Test22&parent_id=32" https://192.168.2.49/api/v4/groups

url = gitlab_url + '/api/v4/groups'

#postData = {
#    'name':'Test22',
#    'path':'Test22',
#    'parent_id':32,
#}
postData = {
    'name':'Test4',
    'path':'Test4',
}

response = requests.post(url,headers=headers,data=postData,verify=False)
print(response.text)



