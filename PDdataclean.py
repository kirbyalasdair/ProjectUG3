import os
import csv

path = 'cabspottingdata'

with open('PdCabData.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    toprow = ['TaxiId','Latitude','Longitude','Occupied','Time']
    writer.writerow(toprow)
    
    for file in os.listdir(path):
        filepath= path + '/' + file
        f = open(filepath, "r")
        taxiId=file.strip('new_')
        taxiId=taxiId.strip('.txt')

        occupied = False
        previous = []
        
        for x in f:
            row = x.split()
            if row[2]== '0':
                if occupied == True:
                    writer.writerow(previous)
                    occupied = False
                else:
                    continue
            else:
                if occupied == True:
                    row.insert(0, taxiId)
                    previous = row
                    continue
                else:            
                    row.insert(0, taxiId)
                    writer.writerow(row)
                    occupied = True
