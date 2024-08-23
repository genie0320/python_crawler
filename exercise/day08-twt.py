#####################
# 현재 트위터는 크롤링이 금지되어 있음.
# https://www.themiilk.com/articles/a70e2d1e9
# 단순 영상 보기로 대체
#####################

import boto3.resources
import requests
from urllib import parse
import json

URL = "https://x.com/i/api/graphql/E3opETHurmVJflFsUBVuUQ/UserTweets"

HEADERS = {
    "x-csrf-token": "c80f37d2ca45df97f8f105c26dc1c0459e504528ee4b4907ce8e15f3a875bda53b5b639552518939257fb78c6c9507cf2fd9545eaddb7239a0e35c3b6cdaad4c8fb968d4baa959e2e4f7ed50eec28048",
    "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
    "cookie": 'guest_id=v1%3A171411388900703227; night_mode=2; guest_id_marketing=v1%3A171411388900703227; guest_id_ads=v1%3A171411388900703227; kdt=uJ2VZEqlWQo1WBG72XPqfQMjK3edSkbvrCrJEgte; auth_token=5fff62f2a70f8b836896723fb738b697286bfe0f; ct0=c80f37d2ca45df97f8f105c26dc1c0459e504528ee4b4907ce8e15f3a875bda53b5b639552518939257fb78c6c9507cf2fd9545eaddb7239a0e35c3b6cdaad4c8fb968d4baa959e2e4f7ed50eec28048; twid=u%3D64573858; lang=ko; personalization_id="v1_BjeEM1/QoFi8ze4UOmysvw=="',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ko-KR,ko;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-US;q=0.6,en;q=0.5",
    "x-client-transaction-id": "qrW/mQCa5H9C+6RP7KONzcFu0tBsB4N6ko5t3BG9kZUatu9V0wpyudKmkRvhUS568tLD3ai9HP4VoeLUAykS0fbq6onAqQ",
    "x-twitter-active-user": "yes",
    "x-twitter-auth-type": "OAuth2Session",
    "x-twitter-client-language": "ko",
    "referer": "https://x.com/BTS_twt",
    "content-type": "application/json",
    "cache-control": "no-cache",
    "dnt": "1",
    "pragma": "no-cache",
    "priority": "u=1, i",
}

# params = {
#     "userId": "1214297432",
#     "count": 20,
#     "includePromotedContent": True,
#     "withQuickPromoteEligibilityTweetFields": True,
#     "withVoice": True,
#     "withV2Timeline": True,
# }

params = {"variables": '{"screen_name":"catdiarys","withSafetyModeUserFields":true}'}
params_text = json.dumps(params)
params_text = parse.quote(params_text)

# URL + "?variables=" + params_text
URL = "https://x.com/i/api/graphql/Yka-W8dz7RaEuQNkroPkYw/UserByScreenName"
response = requests.get(URL, params=params, headers=HEADERS)
# response = requests.get(URL + "?variables=" + params_text, headers=HEADERS)
print(response.status_code)

response.text
