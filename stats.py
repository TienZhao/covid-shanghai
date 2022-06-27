import math, json

count = 0
sum_i = 0
sum_i2 = 0
sum_logi = 0
max = 0
max_name = ""

with open("address.json",'r',encoding='UTF-8') as f:
    addressDict = json.loads(f.read())
    for key in addressDict.keys():
        i = addressDict[key]["count"]
        addressDict[key]["count_adjusted"] = i + 0.2939 * math.sqrt(i)
        # count += 1
        # sum_i += i
        # sum_i2 += i**2
        # sum_logi += (1+ math.log(i))
        # if i > max: 
        #     max = i
        #     max_name = key
    f.close()

# print("count:",count)
# print("sum_i:",sum_i)
# print("sum_i2:",sum_i2)
# print("max",max)
# print("max_name",max_name)

with open("address.json", 'w', encoding='UTF-8') as f:
    f.write(json.dumps(addressDict, ensure_ascii=False, indent=4))