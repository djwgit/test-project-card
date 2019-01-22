# https://developer.github.com/v3/projects/cards/#create-a-project-card
# this python code tries to add a project card to: 
# repo:djwgit/test-project-card 
# project: test-project 
# column: column1 (id:4225464)


import requests
from urllib3.exceptions import InsecureRequestWarning
import json

#################### query projects and columns in a repo #############
def list_projects(token):
    # get all projects under djwgit/test-project-card repo
    _url = "https://api.github.com/repos/djwgit/test-project-card/projects"
    _headers = {
        "Authorization":"token "+token,
        "Accept":"application/vnd.github.inertia-preview+json",
        }

    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    ret = requests.get(url=_url, headers=_headers, verify=False)
    if (not ret.ok):
        print("request failed")
        print(ret.content)
        exit

    # print(ret.content)
    # ---- first project --------
    ret_json = json.loads(ret.content)
    first_project = ret_json[0]
    print(first_project["id"])
    print(first_project["name"])


    # ---------- get columns ------------
    _url = "https://api.github.com/projects/" + str(first_project["id"]) + "/columns"
    _headers = {
        "Authorization":"token "+token,
        "Accept":"application/vnd.github.inertia-preview+json",
        }

    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    ret = requests.get(url=_url, headers=_headers, verify=False)
    if (not ret.ok):
        print("request failed")
        print(ret.content)
        exit

    # print(ret.content)
    # ------ first column --------
    ret_json = json.loads(ret.content)
    first_column = ret_json[0]
    print(first_column["id"])
    print(first_column["name"])
    print(first_column["cards_url"])



#################### try to create a project card in a column #############
def create_project_card(token):
  # the column id is 4225464
  _url = "https://api.github.com/projects/columns/4225464/cards"

  _headers = {
        "Authorization":"token " +token,
        "Accept":"application/vnd.github.inertia-preview+json",
  }

  # try to add an issue as a project card. (there is an issue in the repo)
  #_data = {"content_id":1, "content_type":"Issue"}

  # try to add a note as a project card
  _data = {"content", "just some notes here as a card"}

  requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
  ret = requests.post(url=_url, headers=_headers, data=_data, verify=False)
  if (not ret.ok):
    print("request failed")
    print(ret.content)
    # this is the error msg returned.
    exit

  print(ret.content)


################

# main here
if __name__ == '__main__':
  github_token= "****************"
  
  # this works 
  list_projects(github_token)
  
  # this does not work. error msg:
  # b'{"message":"Problems parsing JSON","documentation_url":"https://developer.github.com/v3/projects/cards/#create-a-project-card"}'
  create_project_card(github_token):
  
  
  
