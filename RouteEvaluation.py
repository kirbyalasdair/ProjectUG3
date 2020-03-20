import os
import csv
import geopy.distance
    
f = open('PDAreaCabData.csv', "r")

linecount = 0

points = []

for x in f:
    x=x.strip()
    row = x.split(',')
    if linecount%2==0:
        linecount +=1
        continue
    else:
        lat= row[1]
        long= row[2]
        points.append((lat,long))
        linecount+=1

def evaluateStops( stops, maxwalk, outputFile):

    xpoints = points
    a = len(xpoints)

    for line in stops:
        lat= line[0]
        long= line[1]

        for y in xpoints:
            distance = geopy.distance.vincenty((lat,long),(y)).km
            if distance < maxwalk:
                points.remove(y)
                
    b=len(xpoints)
    if a>b:
        print('success', a-b)

    with open(outputFile, 'w', newline='') as csvfile:

        writer = csv.writer(csvfile)
        toprow = ['Latitude','Longitude']
        writer.writerow(toprow)

        for point in xpoints:
            writer.writerow(point)
            
    print(outputFile, len(xpoints))

g = open('sfgtfs/stops.txt', 'r')

currentStops = []

lineno=0
for line in g:
    line=line.strip()
    row = line.split(',')
    if lineno == 0:
        lineno +=1
        continue
    else:
        lat= row[0]
        long= row[2]
        currentStops.append((lat,long))

newStops = []

h = open('BusStops/ruralStops.csv', 'r')
i = open('BusStops/urbanStops.csv', 'r')

lineno=0
for line in h:
    line=line.strip()
    row = line.split(',')
    if lineno == 0:
        lineno +=1
        continue
    else:
        lat= row[1]
        long= row[2]
        newStops.append((lat,long))
for line in i:
    line=line.strip()
    row = line.split(',')
    if lineno == 0:
        lineno +=1
        continue
    else:
        lat= row[1]
        long= row[2]
        newStops.append((lat,long))



evaluateStops(newStops,0.142,'new142.csv')
evaluateStops(newStops,0.4,'new400.csv')
