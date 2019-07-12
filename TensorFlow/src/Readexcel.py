'''
Created on Apr 9, 2019

@author: suraj.goenka
'''
import xlrd 
  
loc = ("E:/Text Files/p1.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 1) 
ls = []
for i in range(sheet.nrows): 
    ls.insert(i, sheet.cell_value(i, 3)) 