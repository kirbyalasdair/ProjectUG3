import os
import csv
from datetime import datetime, time
import pytz

linecount = 0
count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

f=open('AreaCabData.csv', 'r')

for x in f:
    x=x.strip()
    row = x.split(',')
    if linecount%2==0:
        linecount +=1
        continue
    else:
        t= row[4]
        t= t.strip('"')
        t = int(t)
        tz = pytz.timezone('PST8PDT')
        dateAndTime = datetime.fromtimestamp(t, tz)
        cabTime = dateAndTime.hour
                            
        count[cabTime] +=1                           
                            
        linecount+=1
print(count)
                 
