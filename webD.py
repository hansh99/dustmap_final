import urllib.request
import json
from pprint import pprint
import pandas as pd

import csv
 
ServiceKey = "sPFZ%2F2MMj1pDhW3LlDmrd%2B7EB05P%2FOdfaq1HX9tQGSAeusrExI%2FKjH3nun3KaTsVyyG2fB4oBjhYPF9Lh1WKcA%3D%3D"

url1 = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc"
category = "/getCtprvnMesureLIst"
url5 = "?itemCode=PM10"
url6 = "&dataGubun=HOUR"
url7 = "&searchCondition=WEEK"
url3 = "&numOfRows=100"
url4 = "&pageNo=1"
url2 = "&serviceKey="
mykey = "sPFZ%2F2MMj1pDhW3LlDmrd%2B7EB05P%2FOdfaq1HX9tQGSAeusrExI%2FKjH3nun3KaTsVyyG2fB4oBjhYPF9Lh1WKcA%3D%3D"

url = url1+category+url5+url6+url7+url4+url3+'&_returnType=json'+url2+mykey

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
    dict = json.loads(response_body.decode('utf-8'))
#    pprint(dict)
else:
    print("Error Code:" + rescode)

dict2=dict['list']
a=dict2[0]

geo={}
geo['busan']=[35.17960000,129.07560000]
geo['chungbuk']=[36.80000000,127.70000000]
geo['chungnam']=[36.51840000,126.80000000]
geo['daegu']=[35.87140000,128.60140000]
geo['daejeon']=[36.37301780,127.24837360]
geo['gangwon']=[37.82280000,128.15550000]
geo['gwangju']=[35.15950000,126.82260000]
geo['gyeongbuk']=[36.49190000,128.88890000]
geo['gyeonggi']=[37.41380000,127.51830000]
geo['gyeongnam']=[35.46606000,128.21320000]
geo['incheon']=[37.45630000,126.70520000]
geo['jeju']=[33.49960000,126.53120000]
geo['jeonbuk']=[35.71750000,127.15300000]
geo['jeonnam']=[34.86790000,126.99100000]
geo['sejong']=[36.48750000,127.28167000]
geo['seoul']=[37.56650000,126.97800000]

mylist=[]

f = open('webDchart.csv', 'w')

writer=csv.writer(f)
writer.writerow(['type','name','price','lat','lon','url'])
url=''
for i in list(a):
    mylist=['0']
    if(i in geo.keys()):
        mylist.pop(0)
        mylist.append('sushi')
        mylist.append(i)
        mylist.append(a[i])
        mylist.append(geo[i][0])
        mylist.append(geo[i][1])

        if (i=='busan'):
            url="http://heis.busan.go.kr/"
        elif (i=='daegu'):
            url="http://www.daejeon.go.kr/hea/index.do"
        elif (i=='chungnam'):
            url="http://air.daegu.go.kr/open_content/ko/index.do"
        elif (i=='chungbuk'):
            url="http://www.chungbuk.go.kr/here/contents.do?key=87544"
        elif (i=='daegu'):
            url="http://www.daejeon.go.kr/hea/index.do"
        elif (i=='daejeon'):
            url="http://www.daejeon.go.kr/hea/index.do"
        elif (i=='chungbuk'):
            url="http://www.chungbuk.go.kr/here/contents.do?key=87544"
        elif (i=='gangwon'):
            url="http://www.airgangwon.go.kr/"
        elif (i=='gwangju'):
            url="http://hevi.gwangju.go.kr/"

        elif (i=='gyeongbuk'):
            url="http://air.gb.go.kr/"
        elif (i=='gyeongnam'):
            url="http://www.gyeongnam.go.kr/knhe/index.gyeong"
        elif (i=='gyeonggi'):
            url="http://air.gg.go.kr/"

        elif (i=='incheon'):
            url="http://air.incheon.go.kr/airinch/inch.html"
        elif (i=='jeju'):
            url="http://web.kma.go.kr/aboutkma/intro/jeju/index.jsp"
        elif (i=='jeonbuk'):
            url="http://air.jeonbuk.go.kr/"
        elif (i=='jeonnam'):
            url="http://www.jihe.go.kr"
        elif (i=='sejong'):
            url="http://www.sejong.go.kr/prog/airInfo/kor/sub04_04_09/last.do"
        elif (i=='seoul'):
            url="http://www.sejong.go.kr/prog/airInfo/kor/sub04_04_09/last.do"
            
        mylist.append(url)
        writer.writerow(mylist)
        mylist=['0']

f.close()

#data=pd.DataFrame(mylist)
#data.to_csv('webDData.csv')
