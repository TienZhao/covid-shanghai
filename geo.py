import json, requests, time
# -*- coding: utf-8 -*-

geoUrl = 'https://restapi.amap.com/v3/geocode/geo'
key = '924b91968e033d46ec03e3897902a6f0'
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

def getGeoArr(arr):
    out = {}
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
                lngLat['lng'] = float(g[0])
                lngLat['R'] = float(g[0])
                lngLat['lat'] = float(g[1])
                lngLat['Q'] = float(g[1])
                out[subArr[i]] = lngLat
            print('Fetched ' + str(subArr))
        else:
            print('[ERROR] on ' + str(subArr))
            print(res)
        time.sleep(0.1)
    return out
