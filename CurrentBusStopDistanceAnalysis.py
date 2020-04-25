import os
import csv
import geopy.distance

path = 'sfgtfs/CutStops'

urban ={}
zeroStops=[]

for file in os.listdir(path):
    filepath= path + '/' + file
    f = open(filepath, "r")
    filename=file.strip('.csv')
          
    linecount = 0
    counts = [0,0,0,0]

    for x in f:
        x=x.strip()
        row = x.split(',')
        if linecount==0:
                linecount +=1
                continue
        else:
            id2=int(eval(row[1]))
            stop= int(eval(row[2]))
            if stop == 0:
                zeroStops.append(id2)
            elif stop < 142:
                counts[0] +=1
            elif stop < 401:
                counts[1] +=1
            elif stop < 501:
                counts[2] +=1
            else:
                counts[3] +=1
    urban[filename] = counts   

   
