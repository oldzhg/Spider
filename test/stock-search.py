import requests
import json
from jsonpath import jsonpath

# start_url = "http://query.sse.com.cn/security/stock/getStockListData.do?&jsonCallBack=jsonpCallback95866&isPagination=true&stockCode=&csrcCode=&areaName=&stockType=1&pageHelp.cacheSize=1&pageHelp.beginPage=1&pageHelp.pageSize=25&pageHelp.pageNo=1&_=1583227415316 "
start_url = 'http://query.sse.com.cn/security/stock/getStockListData.do?stockType=1&pageHelp.pageSize=5'


# type是股票种类 Size是返回页面数量 每页5条信息


def data_output(url):
    headers = {"Referer": "http://www.sse.com.cn/assortment/stock/list/share/"}

    rs = requests.get(url, headers=headers)
    rt = rs.content.decode('utf-8').replace('jsonpCallback95866(', '{"content":').replace('"stockType":"1"})',
                                                                                          '"stockType'
                                                                                          '":"1"}}')
    unicodeStr = json.loads(rt)

    company_Code = jsonpath(unicodeStr, '$..result..COMPANY_CODE')
    company_Name = jsonpath(unicodeStr, '$..result..COMPANY_ABBR')
    company_Date = jsonpath(unicodeStr, '$..result..LISTING_DATE')

    print('公司/A股代码', '\t', '公司/A股简称', '\t', '公司/上市时间')
    for company_Code, company_Name, company_Date in zip(company_Code, company_Name, company_Date):
        print(company_Code, '\t', "\t", company_Name, '\t', '\t', company_Date)


data_output(start_url)
