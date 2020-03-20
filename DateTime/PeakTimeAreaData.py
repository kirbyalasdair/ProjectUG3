import os
import csv
from datetime import datetime
import pytz

path = 'cabspottingdata'

with open('PeakAreaData.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    toprow = ['TaxiId','Latitude','Longitude','Occupied','Time']
    writer.writerow(toprow)
    
    f = open('WeekDayAreaData.csv', "r")

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
        cabTime = dateAndTime.time()

        from datetime import time
        
        peakMorningOn = time(7,30,0)
        peakMorningOff = time(9,30,0)
        peakAfternoonOn = time(16,30,0)
        peakAfternoonOff = time(19,30,0)
        if peakMorningOn < cabTime < peakMorningOff:
            writer.writerow(row)
        elif peakAfternoonOn < cabTime < peakAfternoonOff:
            writer.writerow(row)

        
