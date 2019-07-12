'''
Created on Apr 9, 2019

@author: suraj.goenka
'''
import re
import time
from nltk.corpus import stopwords
from string import punctuation
import xlrd 
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english')) 
loc = ("E:/Text Files/Sample_Data_IA.xlsx") 
input_str = []  
lemmatizer=WordNetLemmatizer()

wb = xlrd.open_workbook(loc) 
print("Total no. of sheets: ",len(wb.sheet_names()))
for k in range(len(wb.sheet_names())):
    sheet = wb.sheet_by_index(k) 
    sheet.cell_value(0, 0) 
    input_str.clear()    
    for j in range(sheet.nrows): 
        input_str.insert(j, sheet.cell_value(j, 3)) 
        
    for i in input_str:
        tokens = word_tokenize(i)
        result = ' '.join(m for m in tokens if not m in stop_words)
        ls=word_tokenize(result.lower())
        print("\n")
        for word in ls:            
            result = ''.join(c for c in word if c not in punctuation)
#             result = re.sub(r'\d+', '', result)
            result = lemmatizer.lemmatize(result)
            print(result, end=" ")
            
#     time.sleep(4)       
wb.release_resources()