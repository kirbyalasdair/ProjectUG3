import os
import csv

f = open('current400.csv', "r")

linecount = 0

stops = []

for x in f:
    x=x.strip()
    row = x.split(',')
    if linecount==0:
        linecount +=1
        continue
    else:
        stops.append(row)
        linecount+=1

g = open('outOfBounds.csv', 'r')

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
            if lat == x[0] and long == x[1]:
                stops.remove(x)
                print('x')
        
with open('current400StopsOutlierFree.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)    
    toprow = ['Latitude','Longitude']
    writer.writerow(toprow)
    
    for x in stops:
        writer.writerow(x)
