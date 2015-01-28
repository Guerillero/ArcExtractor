import dbfread
import csv
import os


def dbf2csv(folder, values, dbfs):
    #
    for i in range(len(values)):
        csvPath = folder + values[i] + ".csv"
        fin = dbfread.open(dbfs[i], load=True)
        fout = open(csvPath, 'w')
        csvFile = csv.writer(fout, dialect=csv.excel)
        # write the header
        csvFile.writerow(fin.field_names)
        #
        for record in fin:
            csvFile.writerow(record.values())
        os.remove(dbfs[i])


def dbf2tsv(folder, values, dbfs):
    # make the csvs
    dbf2csv(folder, values, dbfs)
    # worker loop
    for z in range(len(values)):
        #build the paths for the extraction
        tsvPath = folder + values[z] + ".tsv"
        csvPath = folder + values[z] + ".csv"
        #open the files
        fin = open(csvPath, 'r')
        fout = open(tsvPath, 'w')
        commafile = csv.reader(fin, dialect=csv.excel)
        tabfile = csv.writer(fout, dialect=csv.excel_tab)
        os.remove(csvPath)


def def2xls(path, value, dbfs):
    dbf2csv(path, value, dbfs)
    # TO DO: Excel Support