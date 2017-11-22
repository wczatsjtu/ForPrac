# -*- coding: utf-8 -*-
#接口：http://api.bobo.com/recommend/app/homepage/listLivingInfo?pageNo=1&pageSize=20&platform=1&type=index
import requests
import time

count = 0
open_permission = True
switchStatus = 0 #0:close webview, 1:open webview, 2:switch webveiw url

payload_openview = {'roomId=': '10001198', 'status': '1', 'webViewUrl': 'http://www.weibo.com'}
#r1 = requests.get('http://t02.bobo.com/activity/aprilFool/testApi', params=payload_openview)

while True:
    if switchStatus == 0:
        r = requests.get(
            'http://t02.bobo.com/activity/aprilFool/testApi?roomId=10001225&status=1&webViewUrl=http://www.bobo.com/special/dickytest007/?1511161872500')
        switchStatus = 1
        print "count:", count, "Open Webview, tap on screen to close it"
    elif switchStatus == 1:
        r = requests.get(
            'http://t02.bobo.com/activity/aprilFool/testApi?roomId=10001225&status=1&webViewUrl=http://www.baidu.com')
        switchStatus = 2
        print "count:", count, "Switch Webview"
    else:
        r = requests.get(
            'http://t02.bobo.com/activity/aprilFool/testApi?roomId=10001225&status=0&webViewUrl=http://www.baidu.com')
        switchStatus = 0
        print "count:", count, "Close Webview"
    time.sleep(5)
    count += 1



# #
# while True:
#     r = requests.get(
#         'http://t02.bobo.com/activity/aprilFool/testApi?roomId=10001198&status=1&webViewUrl=http://www.bobo.com/special/dickytest007/?1511161872500')
#     time.sleep(10)
#     count += 1
#     print "count:", count