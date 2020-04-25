import os
import csv
import geopy.distance
    
f = open('sfgtfs/stops.txt', "r")

linecount = 0

points = []
used = []

for x in f:
    x=x.strip()
    row = x.split(',')
    if linecount%2==0:
        linecount +=1
        continue
    else:
        lat= row[0]
        long= row[2]
        points.append((lat,long))
        used.append((lat,long))
        linecount+=1

for point in points:
    removal=[]
    for x in used:
        distance = geopy.distance.vincenty(point,x).km
        if distance < 0.050:
            removal.append(x)
    for y in removal:
        points.remove(y)
        used.remove(y)
        points.append(point)
   


  

with open('newsfgtsStops.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    toprow = ['ID','Latitude','Longitude']
    writer.writerow(toprow)
    i=1
    for point in points:
        
        row=(i,point[0],point[1])
        writer.writerow(row)
        i+=1


