#Souce code to automatically export result of calculation from script.py
from openpyxl import Workbook, load_workbook

import script

wb = Workbook()
ws = wb.active
ws.title = 'Data'

data = script.data

for i in range(len(data)):
        headers = list(data[i].keys())
        values  = list(data[i].values())

        ws.append(headers)
        ws.append(values)


wb.save('test1.xlsx')