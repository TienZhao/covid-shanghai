import os, re, json
import geo

txt_path = "20220413.txt"

fr = open(txt_path, 'r', encoding='UTF-8')
data = fr.read()
passage = data.split('\n')

level = ""
district = ""
for i in range(len(passage)):
    line = passage[i].strip()
    if len(line) < 5:
        matchArr = re.findall(r'(.*?[^小]区)', line, re.M)
        if len(matchArr) > 0:
            district = matchArr[0]
            continue

    if line.find("滑动查看更多") > 0 or line.find("分别居住于") > 0 or line.find("终末消毒措施") > 0:
        continue

    if len(line) > 2:
        address = district
        if line[-1:] in ["、", "，", ",", "。"]:
            address = address + line[:-1] + "，"
        elif line[-1:] != "，" and line[-1:] != "。":
            address = address + line + "，"


        print("居住于" + address)