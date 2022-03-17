import re, json
import geo
# -*- coding: utf-8 -*-

# Read start_date.txt to end_date-1.txt
dateArr = range(20220316, 20220305, -1)
addCount = 0
addArr = []

# Risky areas
midRisks = ['嘉定区娄塘路760弄','徐汇区漕溪北路1200号','浦东新区听悦路920号','闵行区虹梅南路1578号',
            '闵行区思源北路文俊路路口交通大学学生服务中心工地宿舍','金山区学府路1811弄','黄浦区局门后路9号',
            '静安区河南北路233号','浦东新区沪东新村街道长岛路281号']
highRisks = []

# Fix wrong plot locations by replacing the keyword
fixDict = {
    '浦东新区竹园小学（长岛校区）': '浦东新区竹园小学（沪东校区）',
    '闵行区知新村': '闵行区浦江镇知新村',
    '闵行区普联路150弄': '闵行区浦连路150弄',
    '浦东新区南码头东三街35弄': '浦东新区南码头路街道东三街35弄',
    '青浦区崧润路德康雅苑': '青浦区崧润路49弄',
    '青浦区崧润路49弄德康雅苑': '青浦区崧润路49弄',
    '虹口区广灵二路商业二村': '虹口区商业二村',
    '徐汇区田林4村': '徐汇区田林四村',
    '徐汇区宜山路上海精工工地宿舍': '徐汇区宜山路徐家汇中心工地宿舍',
    '嘉定区陇南路嘉涛路停车场': '嘉定区嘉涛路与陇南路交叉口',
    '浦东新区川沙六团七灶北张家宅': '浦东新区川沙新镇七灶村北张家宅',
    '闵行区剑川路中铁四局工地宿舍': '闵行区思源北路文俊路路口交通大学学生服务中心工地宿舍',
    '闵行区思源北路和文俊路路口工地宿舍': '闵行区思源北路文俊路路口交通大学学生服务中心工地宿舍',
    '闵行区剑川路中铁四建工地宿舍': '闵行区思源北路文俊路路口交通大学学生服务中心工地宿舍',
    '闵行区江川路街道剑川路综合服务中心工地宿舍':  '闵行区思源北路文俊路路口交通大学学生服务中心工地宿舍',
    '徐汇区老沪闵路1039弄': '徐汇区老沪闵路1039弄舒乐小区',
    '浦东新区洛神花路6号': '浦东新区南汇新城镇洛神花路白荆路',
    '嘉定区中大街128号': '嘉定区娄塘镇中大街'
}

# Parse addresses from txt
addArr.extend(midRisks)
addArr.extend(highRisks)
for date in dateArr:
    path = str(date) + '.txt'

    fr = open(path, 'r', encoding='UTF-8')
    data = fr.read()
    passage = data.split('\n')

    for line in passage:
        matchArr = re.findall(r'于(.*?)区(.*?)[。，]', line, re.M)
        for addTuple in matchArr:
            addStr = str(addTuple[0]) + '区' + str(addTuple[1])
            addCount += 1
            # Correct wrong address and typo
            if addStr in fixDict:
                addStr = fixDict[addStr]
            print('<li>' + str(addCount) + '. ' + addStr + '</li>')
            if addStr not in addArr:
                addArr.append(addStr)


def updateFile(path, midRisks, highRisks):
    # Update demo.html with new risky area array
    with open(path, 'r+', encoding='utf-8') as f:
        lines = []
        for line in f.readlines():
            startIndexMid = line.find('var midRisks = ')
            startIndexHigh = line.find('var highRisks = ')
            if startIndexMid >= 0:
                lines.append(' '* startIndexMid + 'var midRisks = ' + str(midRisks) + '\n')
            elif startIndexHigh >= 0:
                lines.append(' '* startIndexHigh + 'var highRisks = ' + str(highRisks) + '\n')
            else:
                lines.append(line)
        f.close()

    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
        f.close()


# updateFile('demo.html')
updateFile('shanghai.html', midRisks, highRisks)


res = geo.getGeoArr(addArr)
jsonPath = 'positions.json'
with open(jsonPath, 'w', encoding='utf-8') as f:
    json.dump(res, f, ensure_ascii=False)
    f.close()


print(addArr)
print("共处理" + str(addCount) + "条地址；去重后共计" + str(len(addArr)) + "个地点。")
