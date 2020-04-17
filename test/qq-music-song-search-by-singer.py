import requests
import json

rs = requests.get(
    "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song"
    "&searchid=61886235353531642&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=周杰伦&g_tk=5381&loginUin"
    "=943413047&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8¬ice=0&platform=yqq.json&needNewCode=0")

js = json.loads(rs.content)
list_m = js['data']['song']['list']
for m in list_m:
    print(m['name'])
