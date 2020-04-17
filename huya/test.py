import requests
import re


def get_real_url(rid):
    room_url = 'https://m.huya.com/' + str(rid)
    header = {    'Content-Type': 'application/x-www-form-urlencoded',    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36'    }
    response = requests.get(url=room_url, headers=header)
    pattern = r"hasvedio: '([\s\S]*.m3u8)"
    result = re.findall(pattern, response.text, re.I)
    if result:
        real_url = result[0]
        real_url = re.sub(r'-1_[\s\S]*.m3u8', '-1.m3u8', result[0])
    else:
        real_url = '未开播或直播间不存在'
    return real_url

print(get_real_url('369737'))