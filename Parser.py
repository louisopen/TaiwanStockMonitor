# -*- coding: utf-8 -*-

import argparse
import csv  
import os.path
import re
import string
from datetime import datetime

class Parser():
    def __init__(self, foldername="TWT38U"):
        self.foldername = foldername
        first_day = datetime.today()
        self.today = '{0}/{1:02d}/{2:02d}'.format(first_day.year - 1911, first_day.month, first_day.day)
        
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

    def _change_folder_name(self, foldername):
        ''' Set folder nargsme '''
        self.foldername = foldername

    def _write_data_to_csv(self, row):
        fadd = open('{}.csv'.format(stock_id), 'ab')
        cw = csv.writer(fadd)
        cw.writerow(row)
        fadd.close()

    def _show_row(self, stock_id):
        if True == os.path.isfile('{}/{}.csv'.format(self.foldername, stock_id)):
            f = open('{}/{}.csv'.format(self.foldername, stock_id), 'r')

            for row in csv.reader(f):
                #print self.today
                #print row[0]
                #Only show today information
                if row[0] == self.today:
                    print row
                    self._write_data_to_csv()
            f.close()

    def _parse_data(self, stock_id):
        ''' Parse row from csv file in twt38u '''
        print "個股買賣資訊 - 交易日期、成交股數、成交金額、開盤價、最高價、最低價、收盤價、漲跌價差、成交筆數"
        self._change_folder_name("data")
        self._show_row(stock_id)

    def _parse_twt38u(self, stock_id):
        ''' Parse row from csv file in twt38u '''
        print "外資買賣資訊 - 日期、買量、賣量、總和"
        self._change_folder_name("TWT38U")
        self._show_row(stock_id)

    def _parse_twt43u(self, stock_id):
        ''' Parse row from csv file in twt43u '''
        print "自營商買賣資訊 - 日期、買量、賣量、總和"
        self._change_folder_name("TWT43U")
        self._show_row(stock_id)
        #if True == os.path.isfile('{}/{}.csv'.format(self.foldername, stock_id)):
        #    f = open('{}/{}.csv'.format(self.foldername, stock_id), 'r')
        #    for row in csv.reader(f):
        #        print row
        #    f.close()

    def _parse_twt44u(self, stock_id):
        ''' Parse row from csv file in twt44u '''
        print "投信買賣資訊 - 日期、買量、賣量、總和"
        self._change_folder_name("TWT44U")
        self._show_row(stock_id)

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
    elif len(args.param) == 1:
        stock_id = args.param[0]
    else:
        arguments.error('Not support')
        return

    # Get time of today
    first_day = datetime.today()
    date_str = '{0}/{1:02d}/{2:02d}'.format(first_day.year - 1911, first_day.month, first_day.day)
    parser = Parser()
    #parser._change_line(stock_id)
    parser._parse_data(stock_id)
    parser._parse_twt38u(stock_id)
    parser._parse_twt43u(stock_id)
    parser._parse_twt44u(stock_id)

if __name__ == '__main__':
    main()
