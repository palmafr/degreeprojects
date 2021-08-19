import xlrd
import z3

#Much of the calculating code has been translated from the Java version of it, found at http://francis-palma.net/wp-content/uploads/2016/07/Project.zip

def get_prio(req_set):
    priorities = []

    loc = ("Requirements_gold_and_criteria.xls")
    wb = xlrd.open_workbook(loc)

    if (req_set == "Req_monitor_Priority"):
        sheet = wb.sheet_by_index(10)

    if (req_set == "Req_escape_Priority"):
        sheet = wb.sheet_by_index(7)

    if (req_set == "Req_fall_Priority"):
        sheet = wb.sheet_by_index(4)

    if (req_set == "Req_all_Priority"):
        sheet = wb.sheet_by_index(1)        
 

    sheet.cell_value(0, 1)
    for i in range(sheet.nrows):
        if sheet.cell_value(i, 1) == "Priority":
            continue
        priorities.append([sheet.cell_value(i, 0)])
        temp2 = sheet.cell_value(i, 1)
        priorities[i-1].append([int(temp2)])

    return priorities


