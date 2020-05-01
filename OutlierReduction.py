import os
import csv

f = open('PDAreaCabData.csv', "r")

linecount = 0

stops = []

for x in f:
    x=x.strip()
    row = x.split(',')
    if linecount%2==0:
        linecount +=1
        continue
    else:
        stops.append(row)
        linecount+=1

g = open('BusStops/outOfBounds.csv', 'r')

for x in g:
    x=x.strip()
    row = x.split(',')
    if linecount==0:
        linecount +=1
        continue
    else:
        lat= row[1]
        long= row[2]
        for x in stops:
            if lat == x[1] and long == x[2]:
                stops.remove(x)
        
with open('PDAreaCabDataOutlierFree.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)    
    toprow = ['TaxiId','Latitude','Longitude','Occupied','Time']
    writer.writerow(toprow)
    
    for x in stops:
        writer.writerow(x)
