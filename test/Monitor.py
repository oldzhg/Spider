import requests

log = requests.get("http://140.238.19.103:3000/download/log.txt").text
if log.find("zcy000321@gmail.com") == -1:
    pass
else:
    requests.post("https://sms-api.upyun.com/api/messages",)
    print("ok")

