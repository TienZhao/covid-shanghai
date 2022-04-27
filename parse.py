import os, re, json, datetime
import geo

date = datetime.date.today() - datetime.timedelta(days=1)
date_str = date.strftime('%Y%m%d')
txt_path = date_str + ".txt"
# txt_path = "20220424.txt"
print(txt_path)

fr = open(txt_path, 'r', encoding='UTF-8')
data = fr.read()
passage = data.split('\n')

level = ""
district = ""
body = False
for i in range(len(passage)):
    line = passage[i].strip()
    if len(line) < 5:
        matchArr = re.findall(r'(.*?[^小]区)', line, re.M)
        if len(matchArr) > 0:
            district = matchArr[0]
            continue

    if line.find("滑动查看更多") > 0 or line.find("居住于") > 0 \
            or line.find("终末消毒措施") > 0 or line.find("均已") > 0:
        continue

    if line.find("资料：") >= 0 :
        break

    if line.find("各区信息如下：") >= 0:
        body = True
        continue

    if body and len(line) > 2:
        address = district
        if line[-1:] in ["、", "，", ",", "。"]:
            address = address + line[:-1] + "，"
        elif line[-1:] != "，" and line[-1:] != "。":
            address = address + line + "，"


        print("居住于" + address)