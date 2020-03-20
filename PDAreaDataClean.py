import os
import csv

path = 'cabspottingdata'

with open('PDAreaCabData.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    toprow = ['TaxiId','Latitude','Longitude','Occupied','Time']
    writer.writerow(toprow)
    
    f = open('PdCabData.csv', "r")

    linecount = 0

    for x in f:
        row = x.split(',')
        if linecount==0:
            linecount +=1
            continue        
        elif row[3]== '1':
            lat = float(row[1])
            long = float(row[2])
            if lat < 37.810968 and lat > 37.708130 and long > -122.514657 and long < -122.362724 :
                writer.writerow(row) 
        
