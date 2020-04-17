import requests
import json
import pyperclip


def get_room_uid(key):
    url = 'https://search.cdn.huya.com/?m=Search&do=getSearchContent&v=4&typ=-5&rows=1&q='
    url_search = url + key
    result = requests.get(url_search)
    data = json.loads(result.content)
    return data['response']['1']['docs'][0]['uid']


def get_live(uid):
    live_url = 'https://mp.huya.com/cache.php?m=Live&do=profileRoom&pid=' + str(uid)
    data = json.loads(requests.get(live_url).content)
    return data['data']['stream']['hls']['multiLine'][0]['url']


name = input("输入主播名字或者房间号：")
text = get_live(get_room_uid(name))
print(get_room_uid(name))
print(text)
pyperclip.copy(text)
