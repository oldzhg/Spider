from openpyxl import load_workbook
import requests
import re

base_url = 'https://www.amazon.ae/s?k='

filename = '汇总.xlsx'
wb = load_workbook(filename)  # 打开一个工作簿
sheet = wb['Sheet1']  # 获取表
pattern = re.compile('">AED\s(.*?)</span>')
t = 2501
p = 2510
for i in sheet.iter_rows(min_row=t, max_row=p):

    good_id = i[0].value
    good_id = str(good_id)
    res = requests.get(base_url + good_id)
    good = re.findall(pattern, res.content.decode())
    try:
        if good:
            pos = 'B' + str(t)
            sheet[pos].value = float(good[0])  # 把价格写入到对应的地方
            print("已提取 %d " % t)
            wb.save('汇总.xlsx')
        else:
            pos = 'B' + str(t)
            sheet[pos].value = ''  # 价格为空
            print("已提取 %d " % t)
            wb.save('汇总.xlsx')
    except:
        print(t)
    t = t + 1

print("文件保存完成！")
