# -*- coding: utf-8 -*-
import xlsxwriter
workbook = xlsxwriter.Workbook('DATA.xlsx')
worksheet = workbook.add_worksheet('sheet1')

data = (['text','num1','num2','num3','target'],
        ['A',2,3,4,10],
        ['B',2,5,3,15],
        ['C',1,6,5,20],
        ['A',3,2,6,18],
        ['B',1,3,7,22],
        ['C',4,1,8,25],)
def read_data(source_data):
    for data in source_data:
        yield data

def write_data(source_data):
    for i in range(len(source_data)):
        worksheet.write_row(i,0,tuple(read_data(source_data))[i])

if __name__ == '__main__':
    write_data(data)
    workbook.close()