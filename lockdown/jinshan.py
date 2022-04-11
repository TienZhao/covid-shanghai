import os, re, json
import geo


py_path = os.path.basename(__file__)
txt_input_path = py_path[:py_path.find(".py")] + ".txt"
json_output_path = py_path[:py_path.find(".py")] + ".json"
district = "金山区"

fr = open(txt_input_path, 'r', encoding='UTF-8')
data = fr.read()
passage = data.split('\n')

red_zone = []
yellow_zone = []
green_zone = []

town = ""
for line in passage:
    if len(line) < 6:
        match = re.findall(r'、(.*?镇)', line, re.M)
        if len(match) == 1:
            town = match[0]
    if line.find("封控区：") > -1:
        line_arr = line[4:].split("，")
        for address in line_arr:
            if address.find('、'):
                village = address[0:address.find("村")+1]
                sub_line_arr = address[address.find("村")+1:].split("、")
                for sub_address in sub_line_arr:
                    red_zone.append(district + town + village + address)
            else:
                red_zone.append(district + town + address)
    elif line.find("管控区：") > -1:
        line_arr = line[4:].split("，")
        for address in line_arr:
            if address.find('、'):
                village = address[0:address.find("村") + 1]
                sub_line_arr = address[address.find("村") + 1:].split("、")
                for sub_address in sub_line_arr:
                    yellow_zone.append(district + town + village + address)
            else:
                yellow_zone(district + town + address)


print(red_zone)
print(yellow_zone)
print(green_zone)

res = {
    "red_zone" : geo.getGeoArr(red_zone, 1),
    "yellow_zone" : geo.getGeoArr(yellow_zone, 2),
    "green_zone" : geo.getGeoArr(green_zone, 3),
}
with open(json_output_path, 'w', encoding='utf-8') as f:
    json.dump(res, f, ensure_ascii=False)
    f.close()
