import os
import csv

path = 'cabspottingdata'

with open('AreaCabData.csv', 'w', newline='') as csvfile:

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
            if row[2]== '1':
                row[0] = float(row[0])
                row[1] = float(row[1])
                if row[0] < 37.810968 and row[0] > 37.708130 and row[1] > -122.514657 and row [1] < -122.362724 :
                    row.insert(0, taxiId)
                    writer.writerow(row)    
