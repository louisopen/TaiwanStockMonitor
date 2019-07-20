#!/usr/bin/env python3
#coding=utf-8
#外資及陸資買賣超彙總表
#Installed in Windows by shell
#pip install requests
#pip install pandas
#pip --list
#python --version

from datetime import datetime, timedelta, date
import time
import pandas as pd
#from io import StringIO     #使用內存
import os
import random
import os.path
import json,csv
import requests

#取得當前工作路徑加存檔路徑
workpath = os.path.split(os.path.realpath(__file__))[0]     #windows path + "子目錄"
#股票代碼 (2018/01/08 當日成交值前10檔股票)
#stock_list=[2330,2303]  #請任意新增股票代碼

def get_buy(date):    
    try:
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        headers={"User-Agent":user_agent}
        url_twse='https://www.twse.com.tw/fund/TWT38U?response=jsonl&date=20190716'
        #url_twse='https://www.twse.com.tw/fund/TWT43U?response=jsonl&date=20190716'
        #url_twse='https://www.twse.com.tw/fund/TWT44U?response=jsonl&date=20190716'
        #r=requests.get(url_twse,)    #最後一天OK
        r=requests.get(url_twse, headers=headers)  #日期之外陸資買賣OK

        if len(r.text)<5000:
            print(date+' holiday')
            time.sleep(0.5)
            return None
        else:
            print(date)     #normally
    except:
        print(date +' error')
        time.sleep(0.5)
        return None
        
    data = json.loads(r.text)

    #存檔路徑
    mydir=os.path.join(workpath)
    #filename='外陸資_'+str(year)+'_'+'{0:0=2d}'.format(month)+'.csv'
    filename = date
    if not os.path.isfile(os.path.join(mydir,filename)):    #檢查檔案是否存在
        with open(filename,'w', newline='') as outfile:
            outfile=open(os.path.join(mydir,filename),'w',newline='')
            outputwriter=csv.writer(outfile)
            outputwriter.writerow(data['title'])
            outputwriter.writerow(data['fields'])
            for data in(data['data']):
                outputwriter.writerow(data)
        #outfile.close()     
        print('sussess') 
    else:     
        print('已有相同檔名的檔案存在!!!')

    time.sleep(3 + random.uniform(1,3))

def daterange(start, end):
    for n in range(int ((end - start).days)+1):
        yield start + timedelta(n)

year = 2019
month = 7
start_dt = date(2019, 7, 16)
end_dt = date(year, month, 16)
for dt in daterange(start_dt, end_dt):
    #week =dt.weekday()
    #if week < 5: #星期一是0 ~6  故小於五等於weekday 星期一~日
        dt=dt.strftime('%Y%m%d.csv')    #當地日期時間...格式
        if not os.path.isfile(dt):  #如果檔案尚未被讀取
            get_buy(dt)
        else:
            print(dt+' had ')



