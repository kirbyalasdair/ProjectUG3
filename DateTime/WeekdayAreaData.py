import os
import csv
from datetime import datetime
import pytz

path = 'cabspottingdata'

with open('WeekDayAreaData.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    toprow = ['TaxiId','Latitude','Longitude','Occupied','Time']
    writer.writerow(toprow)
    
    f = open('AreaCabData.csv', "r")

    linecount = 0

    for x in f:
        x=x.strip()
        row = x.split(',')
        if linecount==0:
            linecount +=1
            continue
        t= row[4]
        t= t.strip('"')
        t = int(t)
        tz = pytz.timezone('PST8PDT')
        dateAndTime = datetime.fromtimestamp(t, tz)
        day = dateAndTime.weekday()
        if day < 6:
            writer.writerow(row)

        
