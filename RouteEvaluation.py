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
                xpoints.remove(y)
                
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

"""
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
        
evaluateStops(currentStops,0.142,'Evaluations/current142.csv')
evaluateStops(currentStops,0.4,'Evaluations/current400.csv')
"""

path ='BusStops/Stops'
pairs=[[0,0],[0,0,],[0,0],[0,0],[0,0],[0,0],[0,0]]
pos = 0
for file in os.listdir(path):
    filepath= path + '/' + file
    if file[0] == 'r':
        pairs[pos][0]=filepath
        pos+=1
        if pos == 7:
            pos=0
    else:
        pairs[pos][1]=filepath
        pos+=1

print(pairs)
        
for pair in pairs:    
    newStops = []

    h = open(pair[0], 'r')
    i = open(pair[1], 'r')

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
    lineno=0
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
    address= pair[0]
    address= address.strip('BusStops/Stops/rural')
    address = 'Evaluations/new'+address

    evaluateStops(newStops,0.142,address)

"""
success 732131
Evaluations/new650Stops.csv 133062
success 80112
Evaluations/new700Stops.csv 52950
success 19934
Evaluations/new750Stops.csv 33016
success 11063
Evaluations/new800Stops.csv 21953
success 6816
Evaluations/new850Stops.csv 15137
success 4200
Evaluations/new900Stops.csv 10937
success 4144
Evaluations/new941Stops.csv 6793
"""

