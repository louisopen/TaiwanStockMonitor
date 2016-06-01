# -*- coding: utf-8 -*-

import argparse
import csv  
import os.path

class Parser():
    def __init__(self, foldername="TWT38U"):
        self.foldername = foldername

    def _change_folder_name(self, foldername):
        ''' Set folder nargsme '''
        self.foldername = foldername

    def _show_row(self, stock_id):
        if True == os.path.isfile('{}/{}.csv'.format(self.foldername, stock_id)):
            f = open('{}/{}.csv'.format(self.foldername, stock_id), 'r')
            for row in csv.reader(f):
                print row
            f.close()


    def _parse_twt38u(self, stock_id):
        ''' Parse row from csv file in twt38u '''
        print "外資買賣資訊 - 日期, 買量, 賣量, 總和"
        self._change_folder_name("TWT38U")
        self._show_row(stock_id)

    def _parse_twt43u(self, stock_id):
        ''' Parse row from csv file in twt43u '''
        print "自營商買賣資訊 - 日期, 買量, 賣量, 總和"
        self._change_folder_name("TWT43U")
        self._show_row(stock_id)
        #if True == os.path.isfile('{}/{}.csv'.format(self.foldername, stock_id)):
        #    f = open('{}/{}.csv'.format(self.foldername, stock_id), 'r')
        #    for row in csv.reader(f):
        #        print row
        #    f.close()

    def _parse_twt44u(self, stock_id):
        ''' Parse row from csv file in twt44u '''
        print "投信買賣資訊 - 日期, 買量, 賣量, 總和"
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

    parser = Parser()
    parser._parse_twt38u(stock_id)
    parser._parse_twt43u(stock_id)
    parser._parse_twt44u(stock_id)

if __name__ == '__main__':
    main()
