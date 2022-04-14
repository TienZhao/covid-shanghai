import re, json
import geo
# -*- coding: utf-8 -*-

# Read start_date.txt to end_date-1.txt
lastDate = 20220413
mockDateArr = range(lastDate, lastDate-14, -1)
dateArr = []
for date in mockDateArr:
	if date < 20220401:
		date -= 69
	dateArr.append(date)
addCount = 0
addArr = []
add_dict_arr = []
# days_arr = []

# Risky areas
midRisks = ['黄浦区顺昌路612弄12号', '嘉定区马陆镇康年路261号工地宿舍', '崇明区长兴镇长明村21队',
            '浦东新区北蔡镇联勤村冯桥南宅', '浦东新区日京路88号',
            '浦东新区北蔡镇鹏飞路411弄6号', '嘉定区江桥镇增建村柴中村民组', '闵行区梅陇镇许泾村八组', '崇明区长兴镇新港村15队',
            '闵行区梅陇镇行南村三队', '闵行区华漕镇许浦村三队', '浦东新区康桥镇苗桥路935弄19号',
            '浦东新区御北路235号',]
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
    '闵行区剑川路综合服务中心工地宿舍':  '闵行区思源北路文俊路路口交通大学学生服务中心工地宿舍',
    '徐汇区老沪闵路1039弄': '徐汇区老沪闵路1039弄舒乐小区',
    '浦东新区洛神花路6号': '浦东新区南汇新城镇洛神花路白荆路',
    '嘉定区中大街128号': '嘉定区娄塘镇中大街',
    '闵行区兰平路301弄': '闵行区兰坪路301弄',
    '嘉定区崇教路267号对面工地宿舍': '嘉定区马陆镇康年路261号工地宿舍',
    '崇明区长兴镇长明村21队': '崇明区长兴镇长明村21队西部生活区',
    '松江区中山西路1号': '松江区永丰街道松江中山西路1号',
    '浦东新区东灶路115弄': '浦东新区东八灶115弄',
    '浦东新区秀沿路2弄': '浦东新区秀沿路林海公路交叉口'
}

# Parse addresses from txt
addArr.extend(midRisks)
addArr.extend(highRisks)

mid_dict_arr = [{"add": address, "date": "", "risk": "mid", "label": str("【中风险】" + address), "opacity": 1} for address in midRisks]
high_dict_arr = [{"add": address, "date": "", "risk": "high", "label": str("【高风险】" + address), "opacity": 1} for address in highRisks]
add_dict_arr.extend(mid_dict_arr)
add_dict_arr.extend(high_dict_arr)


# mid_dict_arr = [{"add": address, "style": 0, "name": str("【中风险】" + address)} for address in midRisks]
# high_dict_arr = [{"add": address, "style": 0, "name": str("【高风险】" + address)} for address in highRisks]
# days_arr.append(mid_dict_arr)
# days_arr.append(high_dict_arr)

for date in dateArr:
    # one_day_arr = []
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
                date_in_label = " （" + str(date)[4:6] + "-" + str(date)[6:8] + "）"
                opacity = 0.85 - (dateArr[0] - date) * 0.05
                if opacity == 0.85:
                    opacity = 1
                add_dict_arr.append({"add": addStr, "date": str(date), "risk": "none", "label": str(addStr + date_in_label), "opacity": opacity})
                # one_day_arr.append({"add": addStr, "style": dateArr[0] - date, "name": str(addStr + date_in_label)})
print(add_dict_arr)

    # days_arr.append(one_day_arr)


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


# res = geo.getGeoArr(addArr)
# jsonPath = 'positions.json'
# with open(jsonPath, 'w', encoding='utf-8') as f:
#     json.dump(res, f, ensure_ascii=False)
#     f.close()

# res = geo.getGeoDictArr(add_dict_arr)
# jsonPath = 'positions_new.json'
# with open(jsonPath, 'w', encoding='utf-8') as f:
#     json.dump(res, f, ensure_ascii=False)
#     f.close()

res = geo.getMassGeoDictArr(add_dict_arr)
addLines = [str(r) + ",\n" for r in res]
jsonPath = 'positives.js'
with open(jsonPath, 'w', encoding='utf-8') as f:
    f.write("var positives = [\n")
    f.writelines(addLines)
    f.write("]\n")
    f.close()


print(addArr)
print("共处理" + str(addCount) + "条地址；去重后共计" + str(len(addArr)) + "个地点。")
