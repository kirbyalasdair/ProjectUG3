import os
import csv
from datetime import datetime
import pytz

with open('DeadPDAreaData.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    toprow = ['TaxiId','Latitude','Longitude','Occupied','Time']
    writer.writerow(toprow)
    
    f = open('WeekDaysPDAreaData.csv', "r")

    linecount = 0

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
            cabTime = dateAndTime.time()

            from datetime import time
            
            DeadEnd = time(7,0,0)
            DeadStart = time(2,0,0)
            if DeadStart < cabTime < DeadEnd: 
                writer.writerow(row)
            
            
            linecount+=1
        
