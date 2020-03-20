import os
import csv
from datetime import datetime

path = 'cabspottingdata'

with open('notPeakTimePDAreaCabData.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    toprow = ['TaxiId','Latitude','Longitude','Occupied','Time']
    writer.writerow(toprow)
    
    f = open('WeekDayAreaCabData.csv', "r")

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
        dateAndTime = datetime.fromtimestamp(t) 
        cabTime = dateAndTime.time()

        from datetime import time
        
        peakMorningOn = time(7,30,0)
        peakMorningOff = time(9,30,0)
        peakAfternoonOn = time(16,30,0)
        peakAfternoonOff = time(19,30,0)
        if peakMorningOff < cabTime < peakAfternoonOn:
            writer.writerow(row)
        elif peakAfternoonOff < cabTime: 
            writer.writerow(row)
        elif cabTime < peakMorningOn:
            writer.writerow(row)

        
