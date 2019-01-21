#!/usr/bin/python
import requests
import warnings
warnings.filterwarnings('ignore')

gitlab_url = "https://192.168.2.49"
headers = {"PRIVATE-TOKEN":"JZv7szUDnsWxL888kc7A"}   #duanyuying api

#gitlab_url = "http://192.168.1.85"
#headers = {"PRIVATE-TOKEN":""}   #root api

#curl -k --request DELETE --header "PRIVATE-TOKEN: JZv7szUDnsWxL888kc7A" https://192.168.2.49/api/v4/projects/90

url = gitlab_url + '/api/v4/projects/90'

#postData = {
#    'name':'Test-5',
#    'path':'Test-5',
#    'namespace_id':32,
#}

response = requests.delete(url,headers=headers,verify=False)
print(response.text)

