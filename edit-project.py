#!/usr/bin/python
import requests
import json
import os
import warnings
warnings.filterwarnings('ignore')

gitlab_url = "https://192.168.2.49"
gitlab_ssh = "git@192.168.2.49:"
headers = {"PRIVATE-TOKEN":""}   #duanyuying api

#gitlab_url = "http://192.168.1.85"
#headers = {"PRIVATE-TOKEN":""}   #root api

dict1 = {
'Test2':32,
'Test2/Test22':51,
};
print dict1

git_path = ""
git_id = ""

def createPro(postData):
    '''create project postData
    curl -k --request POST --header "PRIVATE-TOKEN: "  --data "name=Test-7&path=Test-7&namespace_id=32" https://192.168.2.49/api/v4/projects
    '''
    url = gitlab_url + '/api/v4/projects'
    global git_path
    global git_id
    #postData = {
    #    'name':'Test-4',
    #    'path':'Test-4',
    #    'namespace_id':32,
    #}

    response = requests.post(url,headers=headers,data=postData,verify=False)
    #print(response.text)
    data = json.loads(response.text)
    #print data
    #print(data['path_with_namespace'],data['id'])
    git_path = data['path_with_namespace']
    git_id = data['id']
    print(git_path,git_id)

def git_init(git_path):
    git_origin = gitlab_ssh + git_path + '.git'
    print(git_origin)
    os.system('sh git_init.sh ' + git_origin)

def setDefaultBranch(git_id):
    url_branch = gitlab_url + '/api/v4/projects/' + bytes(git_id)
    postData_branch = {
        'default_branch':'dev',
    }
    response = requests.put(url_branch,headers=headers,data=postData_branch,verify=False)
    #print(response.text)
    data = json.loads(response.text)
    #print data
    print(data['path_with_namespace'],data['id'],data['default_branch'])

def setProtectedBranch(git_id):
    os.system('sh protect.sh ' + bytes(git_id) + ' ' + "dev")
    #url_protect = gitlab_url + "/api/v4/projects/" + bytes(git_id) +"/protected_branches?name=dev&push_access_levels=30&merge_access_levels=30"
    #response = requests.post(url_protect,headers=headers,verify=False)
    #print(response.text)


if __name__ == "__main__":
    with open('pro-list','r') as f1:
        list1 = f1.readlines()
    for i in range(0,len(list1)):
        strline = list1[i].strip('\n').split(":")
        Group = strline[0]
        Project = strline[1]
        postData = {
            'name':Project,
            'path':Project,
            'namespace_id':dict1[Group],
        }
        print postData
        createPro(postData)
        git_init(git_path)
        setDefaultBranch(git_id)
        setProtectedBranch(git_id)
 
