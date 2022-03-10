import re
# -*- coding: utf-8 -*-

# Read start_date.txt to end_date-1.txt
dateArr = range(20220306, 20220311)
addCount = 0
addArr = []

# Fix wrong plot locations by replacing the keyword
fixDict = {
    '浦东新区竹园小学（长岛校区）': '浦东新区竹园小学（沪东校区）',
    '闵行区知新村': '闵行区浦江镇知新村',
}

# Parse addresses from txt
for date in dateArr:
    path = str(date) + '.txt'

    fr = open(path, 'r', encoding='UTF-8')
    data = fr.read()
    passage = data.split('\n')

    for line in passage:
        matchArr = re.findall(r'于(.*?)[。，]', line, re.M)
        for addStr in matchArr:
            addCount += 1
            print('<li>' + str(addCount) + '. ' + addStr + '</li>')
            if addStr in fixDict:
                addStr = fixDict[addStr]
            if addStr not in addArr:
                addArr.append(addStr)

# Update demo.html with new address array
with open('demo.html', 'r+', encoding='utf-8') as f:
    lines = []
    for line in f.readlines():
        startIndex = line.find('var adds = ')
        if startIndex >= 0:
            # print(line)
            lines.append(' '* startIndex + 'var adds = ' + str(addArr) + '\n')
        else:
            lines.append(line)
    f.close()

with open('demo.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
    f.close()

print(addArr)
print("共处理" + str(addCount) + "条地址；去重后共计" + str(len(addArr)) + "个地点。")
