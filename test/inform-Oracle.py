import requests

url = "https://iaas.ap-seoul-1.oraclecloud.com/20160918/instances/"

headers = {

    'opc-request-id': 'csid098a35de48a78a2e641a8c32aaf9/f3ac01d8e77d43299b98ef82b9d56baf',
    'accept-language': 'zh-Hans',
    'authorization': 'Signature keyId=\"ST$eyJraWQiOiJhc3dfb2MxXzIwMTktMDYtMjciLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJvY2lkMS51c2VyLm9jMS4uYWFhYWFhYWF1dGNnd3VwdGR0Y2NqY3ZyYTd2aWdnYjRra2xhd2hzMml5eWJlNDR0NGVjc29qeDc0cGpxIiwibWZhX3ZlcmlmaWVkIjoiZmFsc2UiLCJpc3MiOiJhdXRoU2VydmljZS5vcmFjbGUuY29tIiwicHR5cGUiOiJ1c2VyIiwic2Vzc19leHAiOiJNb24sIDIzIE1hciAyMDIwIDA2OjE1OjQ2IFVUQyIsImF1ZCI6Im9jaSIsInBzdHlwZSI6Im5hdHYiLCJ0dHlwZSI6ImxvZ2luIiwiZXhwIjoxNTg0ODY0MzQ4LCJpYXQiOjE1ODQ4NjA3NDgsImp0aSI6ImE2ZDBmNzFhLTczYTAtNDE2Ny1hZmJlLTk4OWM4M2ZlY2U4YyIsInRlbmFudCI6Im9jaWQxLnRlbmFuY3kub2MxLi5hYWFhYWFhYXFsenBxY2hpYnhuamFzemJ5dTI3eGplNW1tZHRlNWZiZnN6eWY2NjNjeHlpZnEzcXRieHEiLCJqd2siOiJ7XCJhbGdcIjpcIlJTMjU2XCIsXCJlXCI6XCJBUUFCXCIsXCJleHRcIjp0cnVlLFwia2V5X29wc1wiOltcInZlcmlmeVwiXSxcImt0eVwiOlwiUlNBXCIsXCJuXCI6XCJyVzNmVGVIM1dHdHlkc2JIM1JUVzNaem8xQkh5TC1OQWk1dnBiRXNDMC1RMmZHX0htLTk3eXNqWGhXVHpJc3VWUW9YV1pPS09NWHB4eFFEbUV3cHh0VkNTZ2NNUE1aWGRfT3hrRVlEakJkbTlEeWRxdkh2d3M5RFNCek15LTZSM3lPTVFqRXRMSjRqQS1wRUVwVGlOYUdpaE1XT2NWUHFab0txSUFaUkVZRTB5Y0Nudlk0VHZZM2xFQ3FCVUtaeGFSYkJ6MHVlY1I1OGRaUXRtWnJrVWNxNk12RF9HSHhjWEJGZ2ZRU3N6LWVRb2ZpR3dCUTB1WVp2QWJzS1ZQN2RZaElia3BEVTRKQl9ybGZvaktTN0M4NDBTV2xjcGRQVXFXb3ZnZV9yTU9nUEJfSWVvZVlpQjRNei1BenJwVDZ2OE1KcjVUM2ZMZUc5RmVPSWUwMF9qa1FcIixcImtpZFwiOlwicHVia2V5LWQwMzc3MDg1LTJiNjAtNDk1MS05MjcyLTg4ZWZjODQ0ODg3N1wifSJ9.o9vNYCpOgfLkU3I-oB0HHQIeCAOJQhn1ERVe80do76dwjGRjjTfLe6e5lw-haS1AlhfgeMUZQg5_OsGHMGFTTBx7Dn5WDnUrq9fIp5drkBSfiszlQFKpvhlUIu6JUqqhDolH0Pg05aBX8wCxXj3ztccga06wAHbnzNtW_qPTbBSJJqdcB5ItXqqBraA5W4DDBVfQzjMkmF4fgCpmBc6uO_vutxWLjQS6qJIj2WuzLVC_h4K3RNd954VOSVSnTpvNCKXIO-Lpm_IF8n6uWLiC6jTR-Oei9tBNJVEmo_m1Dmc6HiOrWB3mZf3gDPtdA17B-1PZNWje-FyOvqiOBMYpWg\",version=\"1\",algorithm=\"rsa-sha256\",headers=\"(request-target) host content-length accept-language content-type opc-request-id x-content-sha256 x-date",signature="dVR+1QolaB3fbd9ZjosP0s6b5pbe8OhknlaK+3XSKE0BYX9P1aXhwGs7/a5tbMlquZzt5ghm24CMmepOsBddr5haYe18JzijQjgVGEwI3xzi2yxnoUI8jd45EMfK5Lx523orEugEVS1jorQO0PMz0/fMSrjiJSrFnCXBDUnSmgEZurn76D+6IjsLmM/nSkvRNMqgMsTpWVjjYtw8BboEShTO59x+lr9H4MUMwgz7+grOqk2SYJGfDW8HbtcBmEy65vaWpl4fvHACiBiQpgrem11WExw5YNCIpBRJOf1QZk6lWbBIP/eaOR/fNVK53zWeQzDPkJX8WexbaL1ZPQrDkQ==\"',
    'Content-Type': 'application/json',
    'x-content-sha256': 'hA8c1mfbe+EaIHgRjUMJ3jGiVqPCYuXQ7lvleYqkIaI=',
    'Sec-Fetch-Dest': 'empty',
    'x-date': 'Sun, 22 Mar 2020 07:16:52 GMT'
}

rs = requests.get(url, headers=headers)

data = {"compartmentId": "ocid1.tenancy.oc1..aaaaaaaaqlzpqchibxnjaszbyu27xje5mmdte5fbfszyf663cxyifq3qtbxq",
        "displayName": "Oracle", "availabilityDomain": "lIAu:AP-SEOUL-1-AD-1", "sourceDetails": {"sourceType": "image",
                                                                                                 "imageId": "ocid1.image.oc1.ap-seoul-1.aaaaaaaazrfma7gwjj36m7vcxeork2azxshoymo4zbi5jfti6zqvcmopix7a"},
        "shape": "VM.Standard.E2.1.Micro", "createVnicDetails": {
        "subnetId": "ocid1.subnet.oc1.ap-seoul-1.aaaaaaaaaf6dweflytmrxqjuhl6nm2gcxqsap3ibcs7er4tem34x7fayu2xa",
        "assignPublicIp": true}, "metadata": {
        "ssh_authorized_keys": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDRabuds44Yf22gof8sMaqRwPlJewLsWjBZzwpI1OF8IC3hwSyZlT+ASeUYGtBiFcYvJzViCzvwarYxiOO64xxZxWXEMnY6JW9iczER5gCUpUSY58N0ywRu3naTGbTgIi2uVXV1Y8MGpQMjFRGPg5HPhj4SRLGV6gYNaejp7kpLe+BpuZoAISc1WcgZhBDZRbDq3HZ/dvINldEK2VIXjyIaiBpsCjvnefchPHySREnPg+8y/vIXUmgEM7fkZOk9e7bIkpuO4dT+BFI1FzQbst6OYGLmixcbRTDJHsT3oHtFoQHPdXQSBa4QUdZSolSX7cbyEzvXHcWjrPc+0w2ZLb/H zcy000321@gmail.com"},
        "agentConfig": {"isMonitoringDisabled": false, "isManagementDisabled": false}, "definedTags": {},
        "freeformTags": {}}

res = requests.post(url, headers=headers, verify=False)
print(res.status_code)
