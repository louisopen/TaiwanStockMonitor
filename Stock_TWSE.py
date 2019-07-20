#!/usr/bin/env python3
#coding=utf-8
#根據每支股票的代碼爬出 成交股數	成交金額	開盤價	最高價	最低價	收盤價	漲跌價差	成交筆數
# Installed in Windows by shell or power shell
# python -m pip install setuptools
# python -m pip install requests
# pip3 install requests 
# python -m pip install beautifulsoup4 
# python -m pip install bs4 
# pip install lxml
# pip --list
# python --version    

# Installed in Linux bash
# sudo apt-get install python3-bs4

import os,time,datetime
import json,csv
import requests
from bs4 import BeautifulSoup as bs
 
#取得當前工作路徑加存檔路徑
workpath = os.path.split(os.path.realpath(__file__))[0] + '\My_Stocks'   #windows path
#股票代碼 (2018/01/08 當日成交值前10檔股票)
stock_list=[2330,2303]  #請任意新增股票代碼
now=datetime.datetime.now()
year_list=range(2019,now.year+1)    #程式會從設定"年"的1月開始抓取資料到現在，每個月份的csv檔
month_list=range(1,13)
 
#建立個股連結(含日期)&抓取資料
def get_data(year, month, stock_id):
   
    date=str(year)+'{0:0=2d}'.format(month)+'01' #格式yyyymmdd  dd只是參考, 都是按mm整個月份的資料
    sid=str(stock_id)
    url_twse='http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date='+str(date)+'&stockNo='+str(stock_id)
    res=requests.post(url_twse,)
    soup=bs(res.text,'lxml')
    data=json.loads(soup.text)
   
    #存檔路徑
    mydir=os.path.join(workpath,str(stock_id),str(year))
    filename='Stock_'+sid+'_'+str(year)+'_'+'{0:0=2d}'.format(month)+'.csv'
    if not os.path.isdir(mydir):      
        os.makedirs(mydir)
     
    if not os.path.isfile(os.path.join(mydir,filename)):    #檢查檔案是否存在
        with open(filename,'w', newline='') as outfile:
            outfile=open(os.path.join(mydir,filename),'w',newline='')
            outputwriter=csv.writer(outfile)
            outputwriter.writerow(data['title'])
            outputwriter.writerow(data['fields'])
            for data in(data['data']):
                outputwriter.writerow(data)
        #outfile.close()      
    else:     
        print('已有相同檔名的檔案存在!!!')
 
time_start=time.time()
for stocks in stock_list:
    for year in year_list:
        for month in month_list:
            if (now.year == year and month > now.month) :break
            get_data(year,month,stocks)
            print(year,month)
            #時間間隔請設3秒以上，以免被twse封鎖
            time.sleep(3)
 
time_end=time.time()
print(time_end-time_start)
