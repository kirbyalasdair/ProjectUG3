import os
import csv
import geopy.distance
import matplotlib.pyplot as plt
import numpy as np

path = 'Clusters'

SSER ={}
SSEU={}

for file in os.listdir(path):
    filepath= path + '/' + file
    f = open(filepath, "r")
    filename=file.strip('.csv')
        
    if filename[0] == 'r':
        k = filename.strip('rural')        
        linecount = 0
        stops = {}
        print(k)
        for i in range(int(k)):
            stops[i] = []

        for x in f:
            x=x.strip()
            row = x.split(',')
            if linecount==0:
                    linecount +=1
                    continue
            else:
                stop= int(eval(row[3]))
                lat= row[1]
                long= row[2]
                stops[stop].append((lat,long))
                linecount+=1    

        stopFile = 'Stops/' + filename + 'Stops.csv'

        with open(stopFile, 'w', newline='') as csvfile:

            writer = csv.writer(csvfile)
            toprow = ['StopId','Latitude','Longitude','count']
            writer.writerow(toprow)

            stopId =0

            for stop in stops:
                points = stops[stop]
                count = len(points)
                lat = 0
                long = 0
                    
                #find mean
                for point in points:
                    lat+=float(eval(point[0]))
                    long+=float(eval(point[1]))
                lat = lat/count
                long = long/count

                #find variance
                SSELat = 0
                SSELong = 0
                for point in points:
                    SSELat += (lat - float(eval(point[0])))**2
                    SSELong += (long - float(eval(point[1])))**2
                SSER[k] = (SSELat, SSELong)
                        
                writer.writerow([stopId,lat,long,count])
                stopId +=1

    if filename[0] == 'u':
        k = filename.strip('urban')        
        linecount = 0
        stops = {}

        print(k)
        for i in range(int(k)):
            stops[i] = []

        for x in f:
            x=x.strip()
            row = x.split(',')
            if linecount==0:
                linecount +=1
                continue
            else:
                stop= int(eval(row[3]))
                lat= row[1]
                long= row[2]
                stops[stop].append((lat,long))
                linecount+=1

        stopFile = 'Stops/' + filename + 'Stops.csv'

        with open(stopFile, 'w', newline='') as csvfile:

            writer = csv.writer(csvfile)
            toprow = ['StopId','Latitude','Longitude','count']
            writer.writerow(toprow)

            stopId =0

            for stop in stops:
                points = stops[stop]
                count = len(points)
                lat = 0
                long = 0
                    
                #find mean
                for point in points:
                    lat+=float(eval(point[0]))
                    long+=float(eval(point[1]))
                lat = lat/count
                long = long/count

                #find variance
                SSELat = 0
                SSELong = 0
                for point in points:
                    SSELat += (lat - float(eval(point[0])))**2
                    SSELong += (long - float(eval(point[1])))**2
                SSEU[k] = (SSELat, SSELong)
                        
                writer.writerow([stopId,lat,long,count])
                stopId +=1    

plt.bar(range(len(SSEU)), list(D.values()), align='center')
plt.xticks(range(len(SSEU)), list(SSEU.keys))
plt.savefig('SSEU.png')
plt.show()

plt.bar(range(len(SSER)), list(D.values()), align='center')
plt.xticks(range(len(SSER)), list(SSER.keys))
plt.savefig('SSER.png')
plt.show()


        
