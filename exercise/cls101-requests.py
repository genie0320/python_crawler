# %%
import requests
from bs4 import BeautifulSoup as bs4
import json
import time


def save_data(data, file_name):
    with open(file_name, "w", encoding="utf8") as json_file:
        json.dump(data, json_file, ensure_ascii=False)

    print(f"{file_name}saveed")


# 영상정보 추출
def get_videos(video_list):
    class_list = []
    for v in video_list["data"]["categoryProductsV3"]["edges"]:
        video = {
            "productId": v["node"]["_id"],
            "class_id": v["node"]["klassId"],
            "clsss_title": v["node"]["title"],
            "categoryId": v["node"]["category"]["id"],
            "categoryTitle": v["node"]["category"]["title"],
            "author": v["node"]["author"]["displayName"],
            "needPay": v["node"]["isTvodOnly"],
            "likeCount": v["node"]["likedCount"],
            "parent": {
                "parentId": v["node"]["category"]["ancestor"]["id"],
                "parentTitle": v["node"]["category"]["ancestor"]["title"],
                # 'depth001'
            },
        }

        class_list.append(video)

    return class_list


def get_lists(categoryId, json_file):
    hasNext = json_file["data"]["categoryProductsV3"]["pageInfo"]["hasNextPage"]
    end_cursor = json_file["data"]["categoryProductsV3"]["pageInfo"]["endCursor"]
    product_list = []

    # while hasNext:
    for i in range(0, 3):
        payload = {
            "operationName": "CategoryProductsV3OnCategoryProductList",
            "variables": '{"filter":{"purchaseOptions":["Lifetime","Rental","Subscription"]},"categoryId":"'
            + categoryId
            + '","first":20,"isLoggedIn":false,"sort":"Recent","originalLanguages":[],"after":"'
            + end_cursor
            + '"}',
            "extensions": '{"persistedQuery":{"version":1,"sha256Hash":"de9123f7372649c2874c9939436d6c5417a48b55af12045b7bdaea7de0a079cc"}}',
        }

        res = requests.post(URL, headers=headers, json=payload)
        res_json = res.json()
        product_list.append(get_videos(res_json))
        hasNext = json_file["data"]["categoryProductsV3"]["pageInfo"]["hasNextPage"]
        print("Go to next page")
    return product_list


# %%
URL = "https://cdn-production-gateway.class101.net/graphql"

headers = {
    "accept": "*/*",
    # "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ko",
    # "apollographql-client-name": "web-prod",
    # "apollographql-operation-type": "query",
    # "cache-control": "no-cache",
    # "content-length": "603",
    # "content-type": "application/json",
    # "cookie": "auid=a677cfb1-536d-40bd-ae1c-2f8e5f7f5743; _fwb=128vOB0RnL45jwJPUpCENTl.1715056641388; ab.storage.deviceId.2b3f474c-7aee-41a1-b6f9-c6be442dd067=%7B%22g%22%3A%2278361901-3a1a-9762-0d8a-469ff5435585%22%2C%22c%22%3A1715056641917%2C%22l%22%3A1715056641917%7D; ch-veil-id=be33a599-6c8b-4d5f-8b55-cbbc893e3898; ab.storage.userId.2b3f474c-7aee-41a1-b6f9-c6be442dd067=%7B%22g%22%3A%22L3jJ4nEavubk4uekbuCNaX7DHBk2%22%2C%22c%22%3A1717477908368%2C%22l%22%3A1717477908368%7D; ajs_anonymous_id=a677cfb1-536d-40bd-ae1c-2f8e5f7f5743; ajs_user_id=L3jJ4nEavubk4uekbuCNaX7DHBk2; ch-session-4864=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZXMiLCJrZXkiOiI0ODY0LTY2YzcwNGJmMTc0MmM0NGEwZjQwIiwiaWF0IjoxNzI0Mzg3OTYzLCJleHAiOjE3MjY5Nzk5NjN9.PZdKTMoubhOP2DskmMj5wlGvkGJJOpKTZPCVvsqTFGg; aws-waf-token=8ed9039f-2427-42e4-947a-7d3e20394b55:AgoAqAoij2gFAAAA:reS8nlsYXDiSTOB3gbzaiGD8gjaBiiOFi7ArUBfSNPBEjZXVDtpmjyjCqZNRh1XKgpLKbrKoperdhBm8P7PEn2tUGEsRT/p3UT6cMROkzVPLhsED/n5mhm3Wd6zYkvKd99OsWkCxs50eQEafm6OmEF5rxHJol6HOradh1P9MbDCBT0aHncCokDcP0TogbR2EkESY7LDbkqoYG3hN6dwWn8KczbGbPgq4mZWA2woefoGmlU1RvUXTBCY6; ab.storage.sessionId.2b3f474c-7aee-41a1-b6f9-c6be442dd067=%7B%22g%22%3A%22ca244a77-31ea-8eef-e9d1-00245f241f0e%22%2C%22e%22%3A1724390880812%2C%22c%22%3A1724373655066%2C%22l%22%3A1724389080812%7D",
    # "dnt": "1",
    # "environment": "WEB",
    # "origin": "https://class101.net",
    # "pragma": "no-cache",
    # "priority": "u=1, i",
    # "referer": "https://class101.net/",
    # "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    # "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-platform": '"Windows"',
    # "sec-fetch-dest": "empty",
    # "sec-fetch-mode": "cors",
    # "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
}
# Load 1 depth menus
payload = {
    "operationName": "CategoriesOnPlusDesktopCategoryTable",
    "variables": {},
    "query": "query CategoriesOnPlusDesktopCategoryTable {\n  categories: categoriesV2ByDepth(depth: 0) {\n    ...CategoryV2OnDesktopCategoryTable\n    children {\n      ...CategoryV2OnDesktopCategoryTable\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment CategoryV2OnDesktopCategoryTable on CategoryV2 {\n  id\n  title\n  depth\n  __typename\n}",
}

res = requests.post(URL, headers=headers, json=payload)

depth000_json = res.json()

depth000s = []
depth001s = []

for menu in depth000_json["data"]["categories"]:
    depth000_id = menu["id"]
    depth000_title = menu["title"]
    depth000s.append(
        {
            "id": depth000_id,
            "title": depth000_title,
        }
    )

    for m in menu["children"]:
        depth001s.append(
            {
                "id": m["id"],
                "title": m["title"],
                "parent": {
                    "parentId": depth000_id,
                    "parentTitle": depth000_title,
                },
            }
        )

# save_data(depth000s, "depth000s.json")
# save_data(depth001s, "depth001s.json")
# %%
for menu in depth001s:
    categoryTitle = menu["title"]
    categoryId = menu["id"]

    # 카테고리의 영상목록 불러오기 - 첫화면
    payload = {
        "operationName": "CategoryProductsV3OnCategoryProductList",
        "variables": '{"filter":{"purchaseOptions":["Lifetime","Rental","Subscription"]},"categoryId":"'
        + categoryId
        + '","first":20,"isLoggedIn":false,"sort":"Recent","originalLanguages":[]}',
        "extensions": '{"persistedQuery":{"version":1,"sha256Hash":"de9123f7372649c2874c9939436d6c5417a48b55af12045b7bdaea7de0a079cc"}}',
    }

    video_res = requests.post(URL, headers=headers, json=payload)
    video_list = video_res.json()

    lists = get_lists(categoryId, video_list)

    print(lists)
    save_data(lists, "text_video.json")
    break
