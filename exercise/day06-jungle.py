import requests
import time
import json

magazineOffset = 0
contestOffset = 0
exhibitOffset = 0
galleryOffset = 0

datas = []

for i in range(3):
    URL = f"https://www.jungle.co.kr/recent.json?magazineOffset={magazineOffset}&contestOffset={contestOffset}&exhibitOffset={exhibitOffset}&galleryOffset={galleryOffset}"
    response = requests.get(URL)
    response_json = response.json()

    articles = response.json()["moreList"]
    _url = "https://www.jungle.co.kr/"

    for art in articles[:1]:
        data = {
            "title": art["title"],
            "date": art["confirmedDate"],
            "cate": art["targetName"],
            "link": _url + art["targetName"] + "/" + str(art["id"]),
        }

        datas.append(data)

    if response_json["existMore"] == False:
        break

    magazineOffset = response_json["magazineOffset"]
    exhibitOffset = response_json["exhibitOffset"]
    contestOffset = response_json["contestOffset"]
    galleryOffset = response_json["galleryOffset"]

    time.sleep(3)

with open("data_jungle.json", "w", encoding="utf8") as json_file:
    json.dump(datas, json_file, indent=4, ensure_ascii=False)
