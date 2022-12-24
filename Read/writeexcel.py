import openpyxl
from openpyxl.workbook import Workbook

wb = Workbook()
print(wb.active.title)
wb['Sheet'].title = "Report for Automation"
sh1 = wb.active
sh1['A1'].value = "Name"
sh1['B1'].value = "Status"
sh1['A2'].value = "Python"
sh1['B2'].value = "Active"
sh1['A3'].value = "Java"
sh1['B3'].value = "ActiveJava1.8.251 Stable Version"
wb.save("FinalWriteExcel.xlsx")

