import re
path = 'C:\\HelloWorld\\covid-shanghai\\20220410.txt'
district = ""
with open(path, 'r+', encoding='utf-8') as f:

    for line in f.readlines():
        matchArr = []
        if len(line) < 6:
            matchArr = re.findall(r'(.*?)区', line, re.M)

        if len(matchArr) > 0:
            district = matchArr[0]
        else:
            if len(line) > 2 and len(line) < 25:
                new_line = '居住于' + district + '区' + line
                print(new_line)


    f.close()