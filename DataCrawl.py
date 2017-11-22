# -*- coding: utf-8 -*-
#接口：http://api.bobo.com/recommend/app/homepage/listLivingInfo?pageNo=1&pageSize=20&platform=1&type=index
import requests
import time
import datetime

file_path = "data1"

payload = {'pageNo': '1', 'pageSize': 200, 'platform': '1', 'type': 'index'}
#r = requests.get('http://api.bobo.com/recommend/app/homepage/listLivingInfo', params=payload)
# print r.encoding
# print r.status_code
# print r.raise_for_status()
# print r.content
# print r.url
# print r.text
# print r.text.__len__()
# print r.json()

print "#############################################################################################"
count = 0
while True:
    with open(file_path, 'a+') as file_data:
        r = requests.get('http://api.bobo.com/recommend/app/homepage/listLivingInfo', params=payload)
#        print "r.content: ", r.content
        print "r.content len:", len(r.content)

        file_data = open(file_path, 'a+')

        file_data.write(str(datetime.datetime.now())+" " )
        file_data.write(str(time.time())+" ")
        file_data.write(r.content)
        ############add a new line#####
        file_data.write('\n')
        # file_data.close()
        count += 1

    print count, datetime.datetime.now()
    time.sleep(600)


# file_data = open(file_path, 'a+')
# file_data.write(r.content)
# ############add a new line#####
# file_data.write('\n')
# file_data.close()


