import os, re, json
import geo


py_path = os.path.basename(__file__)
txt_path = py_path[:py_path.find(".py")] + ".txt"
json_output_path = py_path[:py_path.find(".py")] + ".json"
district = "嘉定区"

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
    if line.find('其余区域') > -1 or line.isdigit():
        continue

    if len(line) > 1 and len(line) < 6:
        if line.find('工业区') > -1:
            town = line[:line.find('工业区') + 3]
            continue
        elif line.find('街道') > -1:
            town = line[:line.find('街道') + 2]
            continue
        elif line.find('新区') > -1:
            town = line[:line.find('新区') + 2]
            continue
        elif line.find('镇') > -1:
            town = line[:line.find('镇') + 1]
            continue
    if line.find("防范区") > -1:
        level = "防范区"
        line = line[line.find('防范区') + 4:]
    elif line.find("管控区") > -1:
        level = "管控区"
        line = line[line.find('管控区') + 4:]
    elif line.find("封控区") > -1:
        level = "封控区"
        line = line[line.find('封控区') + 4:]

    print(line)
    addresses = []
    addresses = line.split('、')
    for a in addresses:
        if len(a) > 0:
            address = district + town + a
            if level == "封控区":
                red_zone.append(address)
            elif level == "管控区":
                yellow_zone.append(address)
            elif level == "防范区":
                green_zone.append(address)
                print(line)

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
