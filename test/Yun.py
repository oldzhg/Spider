import requests
from bs4 import BeautifulSoup
import re
import json
import time

# localtime = time.asctime( time.localtime(time.time()) )
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 '
                  'Safari/537.36'
}

session = requests.session()

login = "https://yuna2.xyz/auth/login"
data = {'email': 'zcy000321@gmail.com', 'passwd': 'zcy5122.'}
req = session.post(login, data=data)

# pattern = r'node/.*/'
# node = "https://yuna2.xyz/user/node"
# res = session.get(node, headers=header)
# nodeList = re.findall(pattern, res.text, re.I)

# count = 20000
# for i in nodeList:
#     count = count + 1
#     url = "https://yuna2.xyz/user/" + i[:-1] + "?ismu=80&relay_rule=0"
#     response = session.get(url=url, headers=header)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     nodeJson = json.loads(soup.find_all("pre")[0].text)
#     nodeJson['local_port'] = count
#     nodeJson = json.dumps(nodeJson)

#     with open('/Users/oldzhg/Surge/test/' + str(count) + '.json', 'w') as f:
#         f.write(nodeJson)
#     print("获取节点中...")

# print("%d个节点获取完毕！" % (count - 20000))
checkUrl = "https://yuna2.xyz/user/checkin"
checkin = session.post(checkUrl)
# ifCheckin = json.loads(checkin.text)
print(checkin)
# if ifCheckin['ret'] == 0:
#     print(ifCheckin['msg'])
# else:
#     print("签到成功！")
