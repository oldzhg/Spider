import requests

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&remoteplace=txt.yqq.lyric&searchid' \
      '=92551292525596106&aggr=0&catZhida=1&lossless=0&sem=1&t=7&p=1&n=5&w=%E5%AD%99%E7%87%95%E5%A7%BF&g_tk=5381' \
      '&loginUin=943413047&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json' \
      '&needNewCode=0 '

re = requests.get(url)
lt = re.json()['data']['lyric']['list']
for i in lt:
    with open('./lyric/' + i['songname'] + '.txt', 'w') as f:
        f.write(i['content'].replace('\\n', '\n'))
    print("next")

