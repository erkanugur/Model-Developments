# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 22:25:24 2020

@author: DELL
"""
# DEPENDENCIES
import pandas as pd
import numpy as np
import os
import random
import re


class read_stocks:
    """
    df = data_import().get_specific_stock_list(stock_name_list = ['GARAN','ACSEL'])
    """

    def __init__(self,column_mapping,
                 path=r'C:\Users\DELL\Desktop\Working_Directory',
                 period_type='Daily',
                 process_date='14.05.2021',extension = 'raw_data'):
        
        date = column_mapping['date']
        open = column_mapping['open']
        high = column_mapping['high']
        low = column_mapping['low']
        close = column_mapping['close']
        stock = column_mapping['stock']
        volume = column_mapping['volume']
        column_list = [date,open,high,low,close,volume]

        excel_file_path = path + r'/' + extension + r'/' + period_type + r'/' + process_date
        excel_file_list = os.listdir(excel_file_path)
        stock_list_default = []
        stock_dict = {}
        for file in excel_file_list:
            file_regex = re.split('[^a-zA-Z]', file)[0]
            stock_list_default.append(file_regex)
            stock_dict[file_regex] = file
        print('Period type = ', period_type)
        print('Process date = ', process_date)
        print('Excel folder path = ', excel_file_path)
        print('Number of files = ', len(excel_file_list))

        self.excel_file_list = excel_file_list
        self.path = path
        self.period_type = period_type
        self.process_date = process_date
        self.excel_file_path = excel_file_path
        self.stock_list_default = stock_list_default
        self.column_list = column_list
        self.stock_dict = stock_dict

    def get_data(self, excel_file_path, file):
        file_regex = re.split('[^a-zA-Z]', file)[0]
        df = pd.read_csv(excel_file_path + r'/' + file, sep=';', header=None)
        df = df.iloc[:,[0,1,2,3,4,7]]
        df.columns = self.column_list
        df.reset_index(inplace=True,drop = True)
        df['stock'] = file_regex
        return df

    def get_specific_stock_list(self, stock_list=['GARAN']):
        not_valid_names = [x for x in stock_list if x not in self.stock_list_default]
        if not_valid_names == []:
            print('Stock name list is valid')
            concat_list = []
            for stock_name in stock_list:
                df_stock = self.get_data(self.excel_file_path, self.stock_dict[stock_name])
                concat_list.append(df_stock)

            df_stocks = pd.concat(concat_list)
            return df_stocks
        else:
            raise ValueError(','.join(not_valid_names) + ' is not valid. Valid stock names are ',
                             self.stock_list_default)

    def get_random_stocks(self, number_of_stocks=5):
        stock_list = random.choices(self.stock_list_default, k=number_of_stocks)
        print('Number of stocks are ' + str(number_of_stocks))
        print('The randomly chosen stocks are ' + ','.join(stock_list))
        concat_list = []
        for stock_name in stock_list:
            df_stock = self.get_data(self.excel_file_path, self.stock_dict[stock_name])
            concat_list.append(df_stock)

        df_stocks = pd.concat(concat_list)
        return df_stocks

    def get_all_stocks(self):
        stock_list = self.stock_list_default
        print('Number of stocks are ' + str(len(stock_list)))
        print('All stocks are ' + ','.join(stock_list))
        concat_list = []
        for stock_name in stock_list:
            df_stock = self.get_data(self.excel_file_path, self.stock_dict[stock_name])
            concat_list.append(df_stock)

        df_stocks = pd.concat(concat_list)
        return df_stocks

    def get_all_stocks_except_list(self, except_list=['CEMAS']):
        all_stock_name_list = self.stock_list_default
        not_valid_names = [x.lower() for x in except_list if x not in all_stock_name_list]
        if not_valid_names == []:
            valid_names = [x for x in all_stock_name_list if x not in except_list]
            print('Except name list is valid')
            print('Number of stocks are ' + str(len(valid_names)))
            print('Excepted stocks are ' + ','.join(except_list))
            concat_list = []
            for stock_name in valid_names:
                df_stock = self.get_data(self.excel_file_path, self.stock_dict[stock_name])
                concat_list.append(df_stock)

            df_stocks = pd.concat(concat_list)
            return df_stocks
        else:
            raise ValueError(','.join(not_valid_names) + ' is not valid. Valid stock names are ',
                             self.stock_list_default)

