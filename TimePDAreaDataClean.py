import os
import csv
from datetime import datetime

path = 'cabspottingdata'

with open('Urban.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    toprow = ['TaxiId','Latitude','Longitude','Occupied','Time']
    writer.writerow(toprow)
    
    f = open('PDAreaCabData.csv', "r")

    linecount = 0

    for x in f:
        row = x.split(',')
        if linecount%2==0:
            linecount +=1
            continue        
        else:
            row[1] = float(row[1])
            row[2] = float(row[2])
            if row[0] > 37.745000 and row[1] > -122.4518:
                writer.writerow(row)
            linecount +=1

        
