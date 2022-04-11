import os,json

red_zone = []
yellow_zone = []
green_zone = []

path_to_json = 'lockdown/'

for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
    with open(path_to_json + file_name, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        red_zone.extend(data["red_zone"])
        yellow_zone.extend(data["yellow_zone"])
        green_zone.extend(data["green_zone"])

print("封控区数量: " + str(len(red_zone)))
print(red_zone)
print("管控区数量: " + str(len(yellow_zone)))
print(yellow_zone)
print("防范区数量: " + str(len(green_zone)))
print(green_zone)

# res = {
#     "red_zone" : red_zone,
#     "yellow_zone" : yellow_zone,
#     "green_zone" : green_zone,
# }

with open('lockdown.js', 'w', encoding='utf-8') as f:
    f.write("var redZone = " + str(red_zone) + "\n")
    f.write("var yellowZone = " + str(yellow_zone) + "\n")
    f.write("var greenZone = " + str(green_zone) + "\n")
    f.close()
