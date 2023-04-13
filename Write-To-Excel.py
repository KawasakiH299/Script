# -*- coding: utf-8 -*-
import xlsxwriter as xw


def xw_toExcel(data, fileName):  # xlsxwriter库储存数据到excel
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    title = ['事务编号', '项']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    for j in range(len(data)):
        insertData = [data[j]["事务编号"], data[j]["项"]]
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        i += 1
    workbook.close()  # 关闭表


# "-------------数据用例-------------"
testData = [
        {"事务编号": 'ID1', "项": "a b c e"},
        {"事务编号": 'ID2', "项": "c d e h"},
        {"事务编号": 'ID3', "项": "a d f h"},
        {"事务编号": 'ID4', "项": "a h"},
        {"事务编号": 'ID5', "项": "b c e"},
        {"事务编号": 'ID6', "项": "a b f h"},
        {"事务编号": 'ID7', "项": "a b f h"},
        {"事务编号": 'ID8', "项": "b d  f h"},
        {"事务编号": 'ID9', "项": "c f g"},


]
fileName = 'DATA.xlsx'
xw_toExcel(testData, fileName)
