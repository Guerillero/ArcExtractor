import dbfread
import csv
import os


def worker(folder, values, dbfs):
    csvList = []

    # turn the array into the paths of the dbfs and the future csvs

    for i in range(len(values)):
        csvList.append(folder + values[i] + ".csv")

    # the stuff happens here
    for z in range(len(dbfs)):
        fin = dbfread.open(dbfs[z], load=True)
        fout = open(csvList[z], 'w')
        csvFile = csv.writer(fout, dialect=csv.excel)
        # write the header
        csvFile.writerow(fin.field_names)
        #
        for record in fin:
            csvFile.writerow(record.values())
        os.remove(dbfs[z])