import json
import requests


def get_form_id():
    urlMsg = 'https://openapi.cpdaily.com/message_pocket_web/V2/mp/restful/mobile/message/extend/get'
    headersMsg = {
        "Content-Type": "application/json",
        "Accesstoken": "8337004e017589dd8f6a7247111bcd96",
        "Appid": "amp-ios-10405"
    }
    bodyMsg = json.dumps({
        "schoolCode": "10405",
        "sign": "b7ad2a635bc691b11efb890da281bf3c",
        "timestamp": 1587000545,
        "userId": "201720330106",
        "page": {
            "start": 0,
            "size": 100
        }
    })
    dataMsg = json.loads(requests.post(url=urlMsg, headers=headersMsg, data=bodyMsg).text)
    msgNewId = dataMsg["msgsNew"][-1]['mobileUrl']
    return msgNewId[-4:]


def get_form_detail():
    urlDetail = 'https://ecut.cpdaily.com/wec-counselor-collector-apps/stu/collector/detailCollector'
    headersDetail = {
        "Content-Type": "application/json",
        "Cookie": "clientType=cpdaily_student; sessionToken=d5827895-2a59-4131-806c-7c4b98c81df1; "
                  "tenantId=ef4b4f8a-d1fd-4f37-a002-27f04ec04ad8; "
                  "MOD_AUTH_CAS=ST-1664204-PLb5XCbU7MrgmGht9Kf61587089291780-igv1-cas; "
                  "acw_tc=76b20fe515870016966331124e68f1df77b59ec7ba3afce547cb0142124634 "
    }
    bodyDetail = json.dumps({
        "collectorWid": "2840"
    })
    dataDetail = json.loads(requests.post(url=urlDetail, headers=headersDetail, data=bodyDetail).text)
    return dataDetail


def post_form(collectWid):
    # 提交学校表单
    # POST https://ecut.cpdaily.com/wec-counselor-collector-apps/stu/collector/submitForm

    try:
        response = requests.post(
            url="https://ecut.cpdaily.com/wec-counselor-collector-apps/stu/collector/submitForm",
            headers={
                "Cpdaily-Extension": "7Q881vmOiX44yXeWnVJf0RsyCeBc/rK+Tn7AeeJkvBjfZvOLlgXH0oxqWtgf "
                                     "krcy4tZ7LRXPBQBWTyD9bolmOd9S5RXZCpYsQtyPMlpDBxaQJJeyInCE3SWX "
                                     "w2CxKcGDSpfF0qRk88E/C+RVV3iNdJk3RlJRnp9ysOpoiIqZYs0XtvF/stAB "
                                     "iikcFNHOBetBGtEu4obpXLuNslyvQEjxIQxf/hhd6G4VkLSaJZUPj2e4jnAK "
                                     "z16p0pNMdgWXhLEn/9c5XiL0LTdQFdZ7U6V2FEmk9MmzPIXm",
                "Cookie": "clientType=cpdaily_student; sessionToken=d5827895-2a59-4131-806c-7c4b98c81df1; "
                          "tenantId=ef4b4f8a-d1fd-4f37-a002-27f04ec04ad8; "
                          "MOD_AUTH_CAS=ST-1678547-sc2gHtdeCuEfL6klBYMt1587111741659-igv1-cas; "
                          "acw_tc=76b20fed15870895616906013e770b9da0c6b73dfe5a40af53972228ea8c3e",
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps({
                "formWid": 676,
                "collectWid": collectWid,
                "form": [
                    {
                        "description": "不要出现空格，如有字母请大写。港澳台及外籍学生，填写身份证号或护照号时，如果字数不够请用*代替",
                        "fieldItems": [

                        ],
                        "isRequired": 1,
                        "imageCount": None,
                        "hasOtherItems": 0,
                        "fieldType": 1,
                        "minLength": 18,
                        "colName": "field001",
                        "title": "你的身份证号",
                        "value": "41150220000321931X",
                        "wid": "2053",
                        "maxLength": 18,
                        "sort": "1",
                        "formWid": "676"
                    },
                    {
                        "description": "请选择所在的省/市/区（县），身处海外地区的同学请选择所在国家。",
                        "fieldItems": [

                        ],
                        "area1": "河南省",
                        "isRequired": 1,
                        "imageCount": -2,
                        "hasOtherItems": 0,
                        "fieldType": 1,
                        "minLength": 1,
                        "colName": "field002",
                        "title": "你的目前所在地",
                        "value": "河南省/信阳市/浉河区",
                        "area2": "信阳市",
                        "wid": "2054",
                        "maxLength": 300,
                        "sort": "2",
                        "area3": "浉河区",
                        "formWid": "676"
                    },
                    {
                        "description": "详细到小区楼号或村庄。例如：江西省南昌市东湖区金茂花园2单元6栋007户",
                        "fieldItems": [

                        ],
                        "isRequired": 1,
                        "imageCount": None,
                        "hasOtherItems": 0,
                        "fieldType": 1,
                        "minLength": 1,
                        "colName": "field003",
                        "title": "你的目前所在地的详细地址",
                        "value": "董家河镇茶叶市场17栋301",
                        "wid": "2055",
                        "maxLength": 300,
                        "sort": "3",
                        "formWid": "676"
                    },
                    {
                        "description": "请测量后如实填写。",
                        "fieldItems": [
                            {
                                "itemWid": "7232",
                                "isSelected": 1,
                                "content": "37.2℃ 及以下",
                                "contendExtend": None,
                                "isOtherItems": 0
                            }
                        ],
                        "isRequired": 1,
                        "imageCount": None,
                        "hasOtherItems": 0,
                        "fieldType": 2,
                        "minLength": 0,
                        "colName": "field004",
                        "title": "你今天的体温是多少？",
                        "value": "37.2℃ 及以下",
                        "wid": "2056",
                        "maxLength": None,
                        "sort": "4",
                        "formWid": "676"
                    },
                    {
                        "description": "",
                        "fieldItems": [
                            {
                                "itemWid": "7235",
                                "isSelected": 1,
                                "content": "没有发热、咳嗽症状",
                                "contendExtend": None,
                                "isOtherItems": 0
                            }
                        ],
                        "isRequired": 1,
                        "imageCount": None,
                        "hasOtherItems": 1,
                        "fieldType": 2,
                        "minLength": 0,
                        "colName": "field005",
                        "title": "是否有发烧、咳嗽等疑似症状？",
                        "value": "没有发热、咳嗽症状",
                        "wid": "2057",
                        "maxLength": None,
                        "sort": "5",
                        "formWid": "676"
                    },
                    {
                        "description": "",
                        "fieldItems": [
                            {
                                "itemWid": "7240",
                                "isSelected": 1,
                                "content": "否",
                                "contendExtend": None,
                                "isOtherItems": 0
                            }
                        ],
                        "isRequired": 1,
                        "imageCount": None,
                        "hasOtherItems": 0,
                        "fieldType": 2,
                        "minLength": 0,
                        "colName": "field006",
                        "title": "近14日是否有湖北接触史？",
                        "value": "否",
                        "wid": "2058",
                        "maxLength": None,
                        "sort": "6",
                        "formWid": "676"
                    },
                    {
                        "description": "",
                        "fieldItems": [
                            {
                                "itemWid": "7242",
                                "isSelected": 1,
                                "content": "否",
                                "contendExtend": None,
                                "isOtherItems": 0
                            }
                        ],
                        "isRequired": 1,
                        "imageCount": None,
                        "hasOtherItems": 0,
                        "fieldType": 2,
                        "minLength": 0,
                        "colName": "field007",
                        "title": "是否接触过新型肺炎疑似或确诊人员？",
                        "value": "否",
                        "wid": "2059",
                        "maxLength": None,
                        "sort": "7",
                        "formWid": "676"
                    },
                    {
                        "description": "",
                        "fieldItems": [
                            {
                                "itemWid": "7244",
                                "isSelected": 1,
                                "content": "是",
                                "contendExtend": None,
                                "isOtherItems": 0
                            }
                        ],
                        "isRequired": 1,
                        "imageCount": None,
                        "hasOtherItems": 0,
                        "fieldType": 2,
                        "minLength": 0,
                        "colName": "field008",
                        "title": "上述信息是我本人填写，本人对上述填写内容的真实性与完整性负责。",
                        "value": "是",
                        "wid": "2060",
                        "maxLength": None,
                        "sort": "8",
                        "formWid": "676"
                    }
                ]
            })
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.text))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


post_form(get_form_id())
