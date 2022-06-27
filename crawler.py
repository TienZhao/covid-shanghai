import time
import requests
from bs4 import BeautifulSoup

urls = []

# 爬虫效果并不好，因为卫健委网站经常有数据黑洞

# 做一个待爬取链接列表
# ['https://wsjkw.sh.gov.cn/xwfb/index.html', 'https://wsjkw.sh.gov.cn/xwfb/index_2.html']
for i in range(1, 14):
    url = "https://wsjkw.sh.gov.cn/xwfb/index"
    if i > 1:
        url = url + "_" + str(i)
    url = url + ".html"
    urls.append(url)
# print(urls)

# 下载
for url in urls:
    # 这个网站对headers的限制好多啊，现成模板都不够，去Chrome里复制了一个出来，还得删掉时间
    my_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "zh_choose=s; wondersLog_zwdt_G_D_I=1551873ba6272ebdf1b95875c2bf0a37-7815; wondersLog_zwdt_sdk=%7B%22persistedTime%22%3A1647682333747%2C%22updatedTime%22%3A1647682341324%2C%22sessionStartTime%22%3A1647682341322%2C%22sessionReferrer%22%3A%22https%3A%2F%2Fzwdtuser.sh.gov.cn%2F%22%2C%22deviceId%22%3A%221551873ba6272ebdf1b95875c2bf0a37-7815%22%2C%22LASTEVENT%22%3A%7B%22eventId%22%3A%22wondersLog_pv%22%2C%22time%22%3A1647682341323%7D%2C%22sessionUuid%22%3A7002267895956256%2C%22costTime%22%3A%7B%7D%7D; zh_choose=s; https_waf_cookie=3bad2873-9d76-4673fbd19336e255957c3d4736d9c1fb77e8; _pk_testcookie.30.0806=1; AlteonP=APEoHWHbHKynKa0ORf9dHw$$; _pk_ref.30.0806=%5B%22%22%2C%22%22%2C1656224414%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DJ_ZFrB9k0MmQaQYpMYcR_m4qsh61p8dwy1smdkKzLa7Svl2S4xexVXrCLvWAem_h%26wd%3D%26eqid%3Dbbcce9f80003f32400000004626255fe%22%5D; _pk_id.30.0806=d8149b6cb18520be.1650611721.5.1656224414.1656224414.; _pk_ses.30.0806=1",
        "Host": "wsjkw.sh.gov.cn",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        }
    res = requests.get(url, headers=my_headers)
    # 保存（调试使用）
    # res.encoding = res.apparent_encoding    # 自动编码
    # with open(r'index.html', 'w+', encoding='utf-8') as f:
    #     f.write(res.text)

    # 使用BS4解析
    soup = BeautifulSoup(res.text, "html.parser")
    # HTML节点树结构：
    # <body> - <div id="container"> - <div id="main"> - <div class="main-container margin-top-15"> - <div class="container"> - <ul class="uli16 nowrapli list-date">
    ul = soup.select_one("body").select_one("#container").select_one("#main").select_one("div.main-container.margin-top-15").select_one("div.container").select_one("ul.uli16.nowrapli.list-date ")
    for li in ul.select('li'):
        a = li.find("a")
        if "无症状感染者居住地" in a['title']:
            print('https://wsjkw.sh.gov.cn' + a['href'] + '; ' + a['title'])
    
    # 睡一会儿
    time.sleep(3)
