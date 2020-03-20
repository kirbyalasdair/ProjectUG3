import os
import csv

path = 'cabspottingdata'

total = 0
  
for file in os.listdir(path):
    filepath= path + '/' + file
    f = open(filepath, "r")
        
    for x in f:
        row = x.split()
        if row[2] == '1':
            total +=1
print(total)
