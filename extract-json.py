# リポジトリーの名前、概要、作成日、更新日、プッシュ日を抽出する
import json

with open("aws-samples-repositories.json") as f:
  repositories = json.load(f)

data = []
for repository in repositories:
  data.append({
    "name": repository["name"],
    "url": repository["url"],
    "description": repository["description"],
    "created_at": repository["created_at"],
    "updated_at": repository["updated_at"],
    "pushed_at": repository["pushed_at"], 
  })

with open("aws-samples-repositories-extracted.json", "w") as f:
  json.dump(data, f)