#!/user/bin/python

import requests
GitIP = 'http://192.168.1.85/api/v4'
rootAPI = "8i4GjEofU3-LzE9rvnZU"
scmuserAPI = "q8pheWznLRncKFszLZy9"
params = {"per_page":"1000"}
headers = {"PRIVATE-TOKEN":scmuserAPI}


url = GitIP + "/projects"
#curl --header "PRIVATE-TOKEN: q8pheWznLRncKFszLZy9" http://192.168.1.85/api/v4/projects
r = requests.get(url,headers=headers,params=params)
data = r.json()
for i in data:
  id = i['id']
  name = i['name']
  namespace = i['name_with_namespace']
  print id,name,namespace

