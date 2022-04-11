import json, requests, time
# -*- coding: utf-8 -*-

geoUrl = 'https://restapi.amap.com/v3/geocode/geo'
key = 'YOUR_AMAP_KEY'
cityCode = '021'


def getGeo(add):
    data = {
        'key': key,
        'address': add,
        'city': cityCode,
        'batch': True,
        'output': 'json'
    }
    res = requests.get(geoUrl, data).json()
    return res

def getGeoArr(arr, style):
    out = []
    for stepStart in range(0, len(arr), 10):
        stepEnd = min(stepStart + 10, len(arr))
        subArr = arr[stepStart: stepEnd]
        addressesStr = '|'.join(subArr)
        res = getGeo(addressesStr)
        if res['status'] == '1' and int(res['count']) == len(subArr):
            for i in range(int(res['count'])):
                geocode = res['geocodes'][i]
                g = geocode['location'].split(',')
                lngLat = {}
                lngLat['lnglat'] = [float(g[0]), float(g[1])]
                lngLat['name'] = subArr[i]
                lngLat['style'] = style
                out.append(lngLat)
            print('Fetched ' + str(subArr))
        else:
            print('[ERROR] on ' + str(subArr))
            print(res)
        time.sleep(0.1)
    return out


def getGeoDictArr(dict_arr):
    out = {}
    for stepStart in range(0, len(dict_arr), 10):
        stepEnd = min(stepStart + 10, len(dict_arr))
        subDictArr = dict_arr[stepStart: stepEnd]
        subAddStrArr = [dict["add"] for dict in subDictArr]
        addressesStr = '|'.join(subAddStrArr)
        res = getGeo(addressesStr)
        if res['status'] == '1' and int(res['count']) == len(subDictArr):
            for i in range(int(res['count'])):
                geocode = res['geocodes'][i]
                g = geocode['location'].split(',')
                # lngLat = {}
                subDictArr[i]['lng'] = float(g[0])
                subDictArr[i]['R'] = float(g[0])
                subDictArr[i]['lat'] = float(g[1])
                subDictArr[i]['Q'] = float(g[1])
                # subDictArr[i] =
                out[subAddStrArr[i]] = subDictArr[i]
            print('Fetched ' + str(subAddStrArr))
        else:
            print('[ERROR] on ' + str(subAddStrArr))
            print(res)
        time.sleep(0.1)
    return out



def getGeoDaysArr(days_arr):
    out = []
    for dict_arr in days_arr:
        day_res = []
        for stepStart in range(0, len(dict_arr), 10):
            stepEnd = min(stepStart + 10, len(dict_arr))
            subDictArr = dict_arr[stepStart: stepEnd]
            subAddStrArr = [dict["add"] for dict in subDictArr]
            addressesStr = '|'.join(subAddStrArr)
            res = getGeo(addressesStr)
            if res['status'] == '1' and int(res['count']) == len(subDictArr):
                for i in range(int(res['count'])):
                    geocode = res['geocodes'][i]
                    g = geocode['location'].split(',')
                    # lngLat = {}
                    subDictArr[i]['lnglat'] = [float(g[0]), float(g[1])]
                    # subDictArr[i] =
                day_res.extend(subDictArr)
                print('Fetched ' + str(subAddStrArr))
            else:
                print('[ERROR] on ' + str(subAddStrArr))
                print(res)
            time.sleep(0.2)

        out.append(day_res)
    return  out


def getMassGeoDictArr(dict_arr):
    out = []
    for stepStart in range(0, len(dict_arr), 10):
        stepEnd = min(stepStart + 10, len(dict_arr))
        subDictArr = dict_arr[stepStart: stepEnd]
        subAddStrArr = [dict["add"] for dict in subDictArr]
        addressesStr = '|'.join(subAddStrArr)
        res = getGeo(addressesStr)
        if res['status'] == '1' and int(res['count']) == len(subDictArr):
            for i in range(int(res['count'])):
                geocode = res['geocodes'][i]
                g = geocode['location'].split(',')
                addDict = {}
                addDict['lnglat'] = [float(g[0]), float(g[1])]
                addDict['name'] = subAddStrArr[i]
                addDict['style'] = 0
                # subDictArr[i] =
                out.append(addDict)
            print('Fetched ' + str(subAddStrArr))
        else:
            print('[ERROR] on ' + str(subAddStrArr))
            print(res)
        time.sleep(0.1)
    return out