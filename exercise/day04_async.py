import re
import requests
import json
from bs4 import BeautifulSoup

URL = "https://n.news.naver.com/article/016/0002349047"

# 네이버 댓글의 경우, 전에 머물던 페이지의 정보를 가지고 댓글정보를 찾아온다. 따라서 referer 정보가 꼭 필요하다.
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ko-KR,ko;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-US;q=0.6,en;q=0.5",
    "referer": "https://n.news.naver.com/article/comment/016/0002349047",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
}

res = requests.get(URL)

if res.status_code == 200:
    data = {}
    # soup 만들기
    soup = BeautifulSoup(res.text, "html.parser")

    # title -----------------------
    title = soup.find("h2", class_="media_end_head_headline").text.strip()
    data["title"] = title

    # content ---------------------
    article_content = soup.find("article", class_="_article_content")

    # 본문내용 외 사진, 소제목 등 삭제
    tag_to_exclude = article_content.find_all(["strong", "span"])
    for tag in tag_to_exclude:
        tag.decompose()

        # 문단 삭제 - 데이터 형태 다듬기
    extracted_text = ""
    for string in article_content.stripped_strings:
        extracted_text += string + " "
    content = extracted_text.strip()

    # 마지막 터치. 이 경우는 [ ] 안의 기자이름, 언론사 이름등 삭제
    data["content"] = re.sub(r"\[.+\]", "", content)

    # reaction ---------------------
    reacts = soup.select_one("ul.u_likeit_layer._faceLayer").select("li")
    react_data = {}
    for el in reacts:
        temp = el.select("a>span")
        react_name = temp[0].text.strip()
        react_num = temp[1].text.strip()
        react_data[react_name] = react_num

    data["reacts"] = react_data

    # comment :

    comments_url = "https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=news&templateId=default_it&pool=cbox5&_cv=20240808151215&_callback=jQuery33103299446841865714_1723776693278&lang=ko&country=KR&objectId=news016%2C0002349047&categoryId=&pageSize=20&indexSize=10&groupId=&listType=OBJECT&pageType=more&page=1&initialize=true&followSize=5&userType=&useAltSort=true&replyPageSize=20&sort=FAVORITE&includeAllStatus=true&_=1723776693280"
    comments_res = requests.get(comments_url, headers=headers)
    comments = comments_res.status_code

    print(comments)
    
    # 여기까지는 막힘이 없었으나, 이 뒤로 url 요소의 params를 떼는 것이 핵심요소였다.
    from urllib.parse import urlparse, parse_qs

    url_param = parse_qs(urlparse(comments_url).query)
    print(url_param)

    print("**************************************************************")
    # print(len(comments))
    # print(len(data))
    # print(data)
else:
    print("Something went wrong")


# json 파일을 만들 때
# with open("data.json", "w") as json_file:
#     json.dump(datas, json_file, indent=4)

# json을 터미널에서 결과로(텍스트) 보고 싶을 때
# print(json.dumps(datas, indent=4))

# 결과를 찍어볼 떄.
# for data in datas:
#     print(data["title"])
#     print(data["body"])
#     print("*******************")
