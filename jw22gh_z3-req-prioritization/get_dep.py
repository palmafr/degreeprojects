import xlrd
import numpy
import z3
from array import *

#Much of the calculating code has been translated from the Java version of it, found at http://francis-palma.net/wp-content/uploads/2016/07/Project.zip


def get_deps(req_set):
    loc = "Requirements_gold_and_criteria.xls"
    wb = xlrd.open_workbook(loc)

    if req_set == "Req_monitor_Depend":
        sheet = wb.sheet_by_index(11)
        req_size = sheet.nrows - 1
        deps = numpy.zeros(shape=(req_size, req_size))

    if req_set == "Req_escape_Depend":
        sheet = wb.sheet_by_index(8)
        req_size = sheet.nrows - 1
        deps = numpy.zeros(shape=(req_size, req_size))

    
    if req_set == "Req_fall_Depend":
        sheet = wb.sheet_by_index(5)
        req_size = sheet.nrows - 1
        deps = numpy.zeros(shape=(req_size, req_size))

    
    if req_set == "Req_all_Depend":
        sheet = wb.sheet_by_index(2)
        req_size = sheet.nrows - 1
        deps = numpy.zeros(shape=(req_size, req_size))    

    for i in range(sheet.nrows):
        if sheet.cell_value(i, 0) == "Req ID":
            continue
        temp = sheet.cell_value(i, 0)
        temp = temp.replace("RT", "")
        temp.lstrip('0')
        temp = int(temp)
        if sheet.cell_value(i, 2):
            temp2 = sheet.cell_value(i, 2)
            temp2 = temp2.replace("RT", "")
            temp2.lstrip('0')
            temp2 = int(temp2)
            deps[temp2 - 1][temp - 1] = 1
            deps[temp - 1][temp2 - 1] = -1
        if sheet.cell_value(i, 3):
            temp3 = sheet.cell_value(i, 3)
            temp3 = temp3.replace("RT", "")
            temp3.lstrip('0')
            temp3 = int(temp3)
            deps[temp3 - 1][temp - 1] = 1
            deps[temp - 1][temp3 - 1] = -1
        if req_set != "Req_monitor_Depend":    
            if sheet.cell_value(i, 4):
             temp4 = sheet.cell_value(i, 4)
             temp4 = temp4.replace("RT", "")
             temp4.lstrip('0')
             temp4 = int(temp4)
             deps[temp4 - 1][temp - 1] = 1
             deps[temp - 1][temp4 - 1] = -1    


    for i in range(req_size):
        for j in range (req_size):
            if deps[i][j] == 1:
                for k in range(req_size):
                    if deps[j][k] == 1:
                        deps[i][k] = 1
                        deps[k][i] = -1
    return deps
