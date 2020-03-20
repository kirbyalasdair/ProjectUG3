import os
import csv

path = 'cabspottingdata'

with open('TrimmedCabData.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    
    for file in os.listdir(path):
        filepath= path + '/' + file
        f = open(filepath, "r")
        taxiId=file.strip('new_')
        taxiId=taxiId.strip('.txt')

        last = [0,0,0]

        toprow = ['TaxiId','Latitude','Longitude','Ocuppied?','Time']
        writer.writerow(toprow)
        
        for x in f:
            row = x.split()
            if row[2]== '0':
                continue
            else:
                if last[0]== row[0] and last[1] == row[1]:
                    continue
                else:
                    last = row
                    row.insert(0, taxiId)                
                    writer.writerow(row)
                    last = row
