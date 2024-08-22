import re
import json
import time
import requests
from bs4 import BeautifulSoup as bs4


def get_infos(URL):

    response = requests.get(URL)

    if response.status_code == 200:
        soup = bs4(response.text, "html.parser")
        datas = {}

        for book in soup.select("ul#yesBestList li"):
            infos = book.select_one(".item_info")

            if infos:
                keywords = []

                title = infos.select_one("a.gd_name").text
                _infos = infos.select(".info_row.info_pubGrp > span")

                if _infos[0].select_one("a"):
                    author = _infos[0].select_one("a").text
                else:
                    author = ""
                publisher = _infos[1].select_one("a").text

                _sellpoint = infos.select_one(".info_row.info_rating span").text
                if "판매지수" in _sellpoint:
                    sellpoint = re.sub(
                        r"판매지수|,",
                        "",
                        _sellpoint,
                    ).strip()
                else:
                    sellpoint = 0

                for k in infos.select(".info_row.info_tag span"):
                    keywords.append(re.sub("#", "", k.select_one("a").text))

                data = {
                    "author": author,
                    "publisher": publisher,
                    "sellpoint": int(sellpoint),
                    "keywords": keywords,
                }

                datas[title] = data

        print(URL)
        print(len(datas))
        return datas

    else:
        print("Error Code:", response.status_code)
        return None


def get_htmls(URL):
    response = requests.get(URL)
    soup = bs4(response.text, "html.parser")

    pages = int(soup.select(".yesUI_pagen")[-1].select("a")[-1].text)

    return pages, soup


# 이하 메인 플로우
URL = "https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001001026&pageNumber=1&pageSize=120"
datas = {}

pages, soup = get_htmls(URL)

for page in range(1, pages + 1):
    _URL = f"https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001001026&pageNumber={page}&pageSize=120"
    datas.update(get_infos(_URL))

    time.sleep(5)

with open("books.json", "w", encoding="utf-8 sig") as json_file:
    json.dump(datas, json_file, indent=4, ensure_ascii=False)
