# %%
# 매번 header를 수정하기가 너무 힘들어서 제작
# TODO: true > True, int > int
def header_converter(text):
    elements = text.split()
    result_dict = {}
    key = None
    value = []

    for element in elements:
        if element.endswith(":"):
            if key is not None:
                result_dict[key.rstrip(":")] = " ".join(value)
            key = element
            value = []
        else:
            value.append(element)

    if key is not None:
        result_dict[key.rstrip(":")] = " ".join(value)

    return result_dict


# %%
text = """
:authority:
cdn-production-gateway.class101.net
:method:
POST
:path:
/graphql
:scheme:
https
accept:
*/*
accept-encoding:
gzip, deflate, br, zstd
accept-language:
ko
apollographql-client-name:
web-prod
apollographql-operation-type:
query
cache-control:
no-cache
content-length:
603
content-type:
application/json
cookie:
auid=a677cfb1-536d-40bd-ae1c-2f8e5f7f5743; _fwb=128vOB0RnL45jwJPUpCENTl.1715056641388; ab.storage.deviceId.2b3f474c-7aee-41a1-b6f9-c6be442dd067=%7B%22g%22%3A%2278361901-3a1a-9762-0d8a-469ff5435585%22%2C%22c%22%3A1715056641917%2C%22l%22%3A1715056641917%7D; ch-veil-id=be33a599-6c8b-4d5f-8b55-cbbc893e3898; ab.storage.userId.2b3f474c-7aee-41a1-b6f9-c6be442dd067=%7B%22g%22%3A%22L3jJ4nEavubk4uekbuCNaX7DHBk2%22%2C%22c%22%3A1717477908368%2C%22l%22%3A1717477908368%7D; ajs_anonymous_id=a677cfb1-536d-40bd-ae1c-2f8e5f7f5743; ajs_user_id=L3jJ4nEavubk4uekbuCNaX7DHBk2; ch-session-4864=eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzZXMiLCJrZXkiOiI0ODY0LTY2YzcwNGJmMTc0MmM0NGEwZjQwIiwiaWF0IjoxNzI0Mzg3OTYzLCJleHAiOjE3MjY5Nzk5NjN9.PZdKTMoubhOP2DskmMj5wlGvkGJJOpKTZPCVvsqTFGg; aws-waf-token=8ed9039f-2427-42e4-947a-7d3e20394b55:AgoAqAoij2gFAAAA:reS8nlsYXDiSTOB3gbzaiGD8gjaBiiOFi7ArUBfSNPBEjZXVDtpmjyjCqZNRh1XKgpLKbrKoperdhBm8P7PEn2tUGEsRT/p3UT6cMROkzVPLhsED/n5mhm3Wd6zYkvKd99OsWkCxs50eQEafm6OmEF5rxHJol6HOradh1P9MbDCBT0aHncCokDcP0TogbR2EkESY7LDbkqoYG3hN6dwWn8KczbGbPgq4mZWA2woefoGmlU1RvUXTBCY6; ab.storage.sessionId.2b3f474c-7aee-41a1-b6f9-c6be442dd067=%7B%22g%22%3A%22ca244a77-31ea-8eef-e9d1-00245f241f0e%22%2C%22e%22%3A1724390880812%2C%22c%22%3A1724373655066%2C%22l%22%3A1724389080812%7D
dnt:
1
environment:
WEB
origin:
https://class101.net
pragma:
no-cache
priority:
u=1, i
referer:
https://class101.net/
sec-ch-ua:
"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"
sec-ch-ua-mobile:
?0
sec-ch-ua-platform:
"Windows"
sec-fetch-dest:
empty
sec-fetch-mode:
cors
sec-fetch-site:
same-site
user-agent:
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36
x-application:
plus
x-auid:
a677cfb1-536d-40bd-ae1c-2f8e5f7f5743
x-request-path:
/ko
x-service-region:
KR
x-ssr-mode:
false
x-tracking-anonymous-id:
a677cfb1-536d-40bd-ae1c-2f8e5f7f5743
x-transaction-id:
8c67ce29-423d-45fb-88d4-29fbcfc57b67
"""

header_converter(text)
# %%
