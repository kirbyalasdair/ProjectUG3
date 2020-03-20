import os
import csv
from datetime import datetime
import pytz

with open('WeekendPDAreaData.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    toprow = ['TaxiId','Latitude','Longitude','Occupied','Time']
    writer.writerow(toprow)
    
    f = open('PDAreaCabData.csv', "r")

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
            day = dateAndTime.weekday()
            if day > 5:
                writer.writerow(row)
            linecount+=1

        
