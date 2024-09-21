import requests
import json

def get_repositories(username):
  repositories = []
  page = 1

  while True:
    url = f'https://api.github.com/users/{username}/repos?page={page}'
    params = {
      "per_page": 100, 
      "page": page
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
      repositories.extend(response.json())
      page += 1
    else:
      break

  return repositories

repositories = get_repositories("aws-samples")
print(f"repositories: {len(repositories)}")

with open("aws-samples-repositories.json", "w") as file:
  json.dump(repositories, file)
#for repository in repositories:
  #print(repository["name"])