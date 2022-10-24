#Souce code to automatically export result of calculation from main_script.py
from openpyxl import Workbook, load_workbook

import main_script

wb = Workbook()
ws = wb.active
ws.title = 'Data'

data = main_script.data

for i in range(len(data)):
        headers = list(data[i].keys())
        values  = list(data[i].values())

        ws.append(headers)
        ws.append(values)


wb.save('test1.xlsx')