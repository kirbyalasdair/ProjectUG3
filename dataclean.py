import os
import csv

path = 'cabspottingdata'

with open('cabData.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)

    toprow = ['TaxiId','Latitude','Longitude','Occupied','Time']
    writer.writerow(toprow)
    
    for file in os.listdir(path):
        filepath= path + '/' + file
        f = open(filepath, "r")
        taxiId=file.strip('new_')
        taxiId=taxiId.strip('.txt')
        
        for x in f:
            row = x.split()
            if row[2]== '0':
                continue
            else:
                row.insert(0, taxiId)
                writer.writerow(row)
