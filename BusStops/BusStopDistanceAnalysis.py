import os
import csv
import geopy.distance

path = 'Distance'

urban ={}
rural={}

for file in os.listdir(path):
    filepath= path + '/' + file
    f = open(filepath, "r")
    filename=file.strip('.csv')
        
    if filename[0] == 'r':        
        linecount = 0
        counts = [0,0,0,0]

        for x in f:
            x=x.strip()
            row = x.split(',')
            if linecount==0:
                    linecount +=1
                    continue
            else:
                stop= int(eval(row[2]))
                if stop < 50:
                    counts[0] +=1
                elif stop < 142:
                    counts[1] +=1
                elif stop < 425:
                    counts[1] +=1
                elif stop < 800:
                    counts[2] +=1
                else:
                    counts[3] +=1
        rural[filename] = counts   

    if filename[0] == 'u':
        k = filename.strip('urban')        
        linecount = 0
        
        counts = [0,0,0,0]

        for x in f:
            x=x.strip()
            row = x.split(',')
            if linecount==0:
                linecount +=1
                continue
            else:
                stop= int(eval(row[2]))
                if stop < 50:
                    counts[0] +=1
                elif stop < 142:
                    counts[1] +=1
                elif stop < 425:
                    counts[1] +=1
                elif stop < 800:
                    counts[2] +=1
                else:
                    counts[3] +=1
        urban[filename] = counts
