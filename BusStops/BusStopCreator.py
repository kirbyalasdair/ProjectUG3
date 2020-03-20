import os
import csv
import geopy.distance
    
f = open('cluster450.csv', "r")

linecount = 0

stops = {}

for i in range(3535):
    stops[i] = []

for x in f:
    x=x.strip()
    row = x.split(',')
    if linecount==0:
        linecount +=1
        continue
    else:
        stop= int(eval(row[5]))
        lat= row[1]
        long= row[2]
        stops[stop].append((lat,long))
        linecount+=1

with open('BusStops.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    toprow = ['StopId','Latitude','Longitude','count']
    writer.writerow(toprow)

    stopId =0

    for stop in stops:
        points = stops[stop]
        count = len(points)
        lat = 0
        long = 0
        for point in points:
            lat+=float(eval(point[0]))
            long+=float(eval(point[1]))
        lat = lat/count
        long = long/count
            
        writer.writerow([stopId,lat,long,count])

        stopId +=1

        
