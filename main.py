import re

dateArr = range(20220306, 20220311)
addCount = 0
addArr = []
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
            if addStr not in addArr:
                addArr.append(addStr)

print(addArr)
print("共处理" + str(addCount) + "条地址；去重后共计" + str(len(addArr)) + "个地点。")
