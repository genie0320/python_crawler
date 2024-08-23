import requests
import json
import boto3

datas = []
start_url = f"https://www.folin.co/api/story?page=1"
response = requests.get(start_url)

res_json = response.json()
total = res_json["page"]["total"]

# for page in range(1, total+1):
for page in range(1, 3):
    URL = f"https://www.folin.co/api/story?page={page}"
    response = requests.get(URL)

    response_json = response.json()

    for item in response_json["items"]["recent_items"]:
        art_id = item["id"]

        people = []
        for person in item["Item"]["Linkers"]:
            _people = {
                "name": person["Linker"]["name"],
                "title": person["Linker"]["title"],
            }
            people.append(_people)

        data = {
            "art_id": art_id,
            "book_name": item["Book"]["Item"]["title"],
            "art_name": item["Item"]["title"],
            "date": item["Item"]["opened_at"],
            "summary": item["summary"],
            "url": "https://www.folin.co/article/" + str(art_id),
            "people": people,
        }

        datas.append(data)

# 파일로 저장
with open("folin.json", "w", encoding="UTF-8 sig") as json_file:
    json.dump(datas, json_file, ensure_ascii=False, indent=4)


# AWS에 업로드
s3 = boto3.resource("s3")

body = open("folin.json", "rb")
s3.Bucket("test-codi42-python").put_object(Key="folin.json", Body=body)
