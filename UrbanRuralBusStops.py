import os
import csv
from datetime import datetime
    
f = open('sfgtfs/stops.txt', "r")

linecount = 0
urbanStops = 0
ruralStops = 0

for x in f:
    row = x.split(',')
    if linecount==0:
        linecount +=1
        continue        
    else:
        row[0] = float(row[0])
        row[2] = float(row[2])
        if row[0] > 37.745000 and row[2] > -122.451800:
            urbanStops+=1
        else:
            ruralStops+=1

print('rural', ruralStops)
print('urban', urbanStops)
