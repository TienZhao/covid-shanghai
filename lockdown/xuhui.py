import os, re, json
import geo


py_path = os.path.basename(__file__)
txt_path = py_path[:py_path.find(".py")] + ".txt"
json_output_path = py_path[:py_path.find(".py")] + ".json"
district = "徐汇区"

fr = open(txt_path, 'r', encoding='UTF-8')
data = fr.read()
passage = data.split('\n')

red_zone = []
yellow_zone = []
green_zone = []

level = ""
town = ""
for i in range(len(passage)):
    line = passage[i].strip()
    if line == "管控区" or line == "防范区":
        level = line
        # print(town, level)
        continue
    elif line.find('街道') > -1:
        town = line
        continue
    elif line.find("其余区域") > -1:
        continue
    elif line.find("咨询电话") > -1:
        continue

    if len(line) < 6 and line.isdigit():
        j = 1
        valid_j = 0
        address = district + town
        while valid_j < 1:
            if passage[i + j].strip():
                valid_j += 1
                valid_line = passage[i + j].strip()
                if len(valid_line) > 0:
                    address += valid_line
                    print(address)
                    if level == "封控区":
                        red_zone.append(address)
                    elif level == "管控区":
                        yellow_zone.append(address)
                    elif level == "防范区":
                        green_zone.append(address)
                    i += j
                else:
                    break
            j += 1

print("封控区数量: " + str(len(red_zone)))
print(red_zone)
print("管控区数量: " + str(len(yellow_zone)))
print(yellow_zone)
print("防范区数量: " + str(len(green_zone)))
print(green_zone)

res = {
    "red_zone" : geo.getGeoArr(red_zone, 1),
    "yellow_zone" : geo.getGeoArr(yellow_zone, 2),
    "green_zone" : geo.getGeoArr(green_zone, 3),
}
with open(json_output_path, 'w', encoding='utf-8') as f:
    json.dump(res, f, ensure_ascii=False)
    f.close()
