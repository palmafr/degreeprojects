import xlrd

#Much of the calculating code has been translated from the Java version of it, found at http://francis-palma.net/wp-content/uploads/2016/07/Project.zip

def get_GS(req_set):
    gold_standard = []

    loc = "Requirements_gold_and_criteria.xls"
    wb = xlrd.open_workbook(loc)

    if req_set == "Req_monitor_gold":
        sheet = wb.sheet_by_index(9)

    if req_set == "Req_escape_gold":
        sheet = wb.sheet_by_index(6)

    if req_set == "Req_fall_gold":
        sheet = wb.sheet_by_index(3)

    if req_set == "Req_all_gold":
        sheet = wb.sheet_by_index(0)        

    sheet.cell_value(0, 0)
    for i in range(sheet.nrows):
        if sheet.cell_value(i, 0) == "Req ID":
            continue
        temp = sheet.cell_value(i, 0)
        gold_standard.append(temp)

    return gold_standard
