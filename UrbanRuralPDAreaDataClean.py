import os
import csv
from datetime import datetime

with open('Urban.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    toprow = ['TaxiId','Latitude','Longitude','Occupied','Time']
    writer.writerow(toprow)
    
    f = open('PDAreaCabDataOutlierFree.csv', "r")

    linecount = 0

    for x in f:
        row = x.split(',')
        if linecount%2==0:
            linecount +=1
            continue        
        else:
            row[1] = float(row[1])
            row[2] = float(row[2])
            if row[1] > 37.745000 and row[2] > -122.451800:
                writer.writerow(row)
            linecount +=1

with open('Rural.csv', 'w', newline='') as csvfile:

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
            linecount +=1
            row[1] = float(row[1])
            row[2] = float(row[2])
            if row[1] > 37.745000 and row[2] > -122.451800:
                continue
            else:
                writer.writerow(row)
            

        
