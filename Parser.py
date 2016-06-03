# -*- coding: utf-8 -*-

import argparse
import csv  
import os.path
import re
import string
from datetime import datetime
from os import mkdir
from os.path import isdir

class Parser():
    def __init__(self, foldername="TWT38U"):
        self.foldername = foldername
        first_day = datetime.today()
        self.day = '{0}/{1:02d}/{2:02d}'.format(first_day.year - 1911, first_day.month, first_day.day)
        
    def _record(self, stock_id, row):
        ''' Save row to csv file '''
        if True == os.path.isfile('{}/{}.csv'.format(self.foldername, stock_id)):
            f = open('{}/{}.csv'.format(self.foldername, stock_id), 'r')
            for row in csv.reader(f):
                print row
            f.close()


        f = open('{}.csv'.format(stock_id), 'ab')
        cw = csv.writer(f, lineterminator='\n')
        cw.writerow(row)
        f.close()

    def _change_day(self, first_day):
        self.day = '{0}/{1:02d}/{2:02d}'.format(first_day.year - 1911, first_day.month, first_day.day)

    def _change_folder_name(self, foldername):
        ''' Set folder nargsme '''
        self.foldername = foldername

    def _write_data_to_csv(self, stock_id, row):
        monitor_folder_name="monitor"
        if not isdir(monitor_folder_name): #hard code "output" first
            mkdir(monitor_folder_name)
        fadd = open('{}/{}.csv'.format(monitor_folder_name, stock_id), 'ab')
        cw = csv.writer(fadd)
        cw.writerow(row)
        fadd.close()

    def _show_row(self, foldername, stock_id):
        self._change_folder_name(foldername)
        if True == os.path.isfile('{}/{}.csv'.format(self.foldername, stock_id)):
            f = open('{}/{}.csv'.format(self.foldername, stock_id), 'r')

            for row in csv.reader(f):
                #print self.day
                #print row[0]
                if row[0] == self.day:
                    print row
                    self._write_data_to_csv(stock_id, row)
            f.close()
            return row
    def _show_human_readable_information(self, tag_list, data):
        if data == None:
            return
        for x in range(len(data)):
            output = "(%s,%s)," %(tag_list[x],data[x])
            print output 

    def _parse_data(self, stock_id):
        ''' Parse row from csv file in twt38u '''
        print "個股買賣資訊 - 交易日期、成交股數、成交金額、開盤價、最高價、最低價、收盤價、漲跌價差、成交筆數"
        #self._change_folder_name("data")
        data = self._show_row("data", stock_id)
        tag_list = ["交易日期","成交股數","成交金額","開盤價","最高價","最低價","收盤價","漲跌價差","成交筆數"]
        self._show_human_readable_information(tag_list, data)

    def _parse_twt38u(self, stock_id):
        ''' Parse row from csv file in twt38u '''
        print "外資買賣資訊 - 日期、買量、賣量、總和"
        #self._change_folder_name("TWT38U")
        data = self._show_row("TWT38U", stock_id)
        tag_list = ["交易日期","買量","賣量","總和"]
        self._show_human_readable_information(tag_list, data)

    def _parse_twt43u(self, stock_id):
        ''' Parse row from csv file in twt43u '''
        print "自營商買賣資訊 - 日期、買量、賣量、總和"
        #self._change_folder_name("TWT43U")
        data = self._show_row("TWT43U", stock_id)
        tag_list = ["交易日期","買量","賣量","總和"]
        self._show_human_readable_information(tag_list, data)
        
    def _parse_twt44u(self, stock_id):
        ''' Parse row from csv file in twt44u '''
        print "投信買賣資訊 - 日期、買量、賣量、總和"
        #self._change_folder_name("TWT44U")
        data = self._show_row("TWT44U", stock_id)
        tag_list = ["交易日期","買量","賣量","總和"]
        self._show_human_readable_information(tag_list, data)

def main():
    # Get arguments
    arguments = argparse.ArgumentParser(description='Parse information by stock id')
    arguments.add_argument('param', type=int, nargs='*',
        help='assigned stock id, default is 2498')
    #arguments.add_argument('-b', '--back', action='store_true',
    #    help='crawl back from assigned day until 2004/2/11')

    args = arguments.parse_args()

    # Day only accept 0 or 3 arguments
    if len(args.param) == 0:
        stock_id = "2498" 
        first_day = datetime.today()
    elif len(args.param) == 1:
        stock_id = args.param[0]
        first_day = datetime.today()
    elif len(args.param) == 4:
        stock_id = args.param[0]
        first_day = datetime(args.param[1], args.param[2], args.param[3])
    else:
        arguments.error('python Parser.py 2454 2016 6 3')
        return

    # Get time of today
    date_str = '{0}/{1:02d}/{2:02d}'.format(first_day.year - 1911, first_day.month, first_day.day)
    parser = Parser()
    #parser._change_line(stock_id)
    parser._change_day(first_day)
    parser._parse_data(stock_id)
    parser._parse_twt38u(stock_id)
    parser._parse_twt43u(stock_id)
    parser._parse_twt44u(stock_id)

if __name__ == '__main__':
    main()
