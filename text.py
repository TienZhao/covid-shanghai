import re
for date in range(20220509, 20220510):
    path = 'C:\\HelloWorld\\covid-shanghai\\txt_by_date\\' + str(date) + '.txt'
    print(str(date))

    district = ""
    new_lines = []
    with open(path, 'r+', encoding='utf-8') as f:
        risk = False

        for line in f.readlines():


            if '消毒' in line and '措施' in line: continue
            if '各区信息如下' in line: continue
            if '资料：' in line: continue
            if '编辑：' in line: continue
            if '个）'  in line: continue
            if '文章已于' in line: continue
            if '扫一扫' in line: continue
            if '公众号' in line: continue
            if '滑动查看'  in line: continue
            if '分别居住于'  in line: continue

            # line = line[:-1]
            line = line.strip()
            if '已通报' in line:
                line = line[:line.find('（')]
                
            if line[-1:] in ["，", "。", "、"]:
                line = line[:-1]   
                
            if '上海市当前中风险等级地区' in line:
                risk = True
                continue

            matchArr = []
            
            isDistrict = False
            if len(line) < 5:
                districts = ["黄浦区", "徐汇区", "静安区", "长宁区", "普陀区", "虹口区", "杨浦区", "浦东新区", "闵行区", "宝山区", "嘉定区", "金山区", "松江区", "青浦区", "奉贤区", "崇明区", "崇明县"]
                for d in districts:
                    if d in line:
                        district = d
                        isDistrict = True
                        break
                
            
            if len(line) > 2 and not isDistrict:
                new_line = '居住于' + district + line + '，\n'
                print(new_line)
                new_lines.append(new_line)
        
            # if '居住地为' in line:
            #     add = line[4:]
            #     new_line = '居住于' + add + '，\n'
            #     print(new_line)
            #     # new_line = '\"' + add + '\": {"add": "' + add + '\", "type": "positive"},'
            #     new_lines.append(new_line)
            # elif '居住于' in line:
            #     add = line[3:]
            #     new_line = '居住于' + add + '，\n'
            #     print(new_line)
            #     # new_line = '\"' + add + '\": {"add": "' + add + '\", "type": "positive"},'
            #     new_lines.append(new_line)

        f.close()

    path = 'C:\\HelloWorld\\covid-shanghai\\' + str(date) + '.txt'
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)