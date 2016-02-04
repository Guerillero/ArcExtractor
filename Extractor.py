##################################################################
# Extract a dbtable for every instance of a value in a geo-file  #
# Written by Thomas Fish                                         #
# Released under the MIT License                                 #
#                                                                #
#                 FOR ARCMAP 10.X ONLY                           #
##################################################################
__Version__ = "1.0.0"

import arcpy
import FileTransformations

# declare map
mxd = arcpy.mapping.MapDocument("CURRENT")


# Import data from ArcMap
fileToConvert = arcpy.GetParameterAsText(0)  # shapefile or GeoDatabase
listFieldValues = arcpy.GetParameterAsText(1)  # text file
outLocation = arcpy.GetParameterAsText(2)  # folder
fieldName = arcpy.GetParameterAsText(3)  # text field
spreadsheetType = arcpy.GetParameterAsText(4)  # text field -- Valid responses are dbf or csv

# translate file into layer
lyr = arcpy.mapping.Layer(fileToConvert)
lyr.name = "MyFile"

# declare arrays for this script
fieldValues = []
fileName = []
filePath = []

# declare the file to open
fin = open(listFieldValues)

# tell end user if there is an error
if fin.closed:
    arcpy.AddMessage("ERROR: File failed to open")

for line in fin:
    # Turn each line in the file into an entry to the array
    lineClear = str.strip(line)
    fieldValues.append(lineClear)

# make file names from UIDs
for i in range(len(fieldValues)):
        fileName.append(fieldValues[i] + ".dbf")

for y in range(len(fileName)):
        filePath.append(outLocation + "\\" + fileName[y])

for z in range(len(fieldValues)):
    # Extract out only the entries that are wanted
    arcpy.AddMessage("Currently extracting " + fieldValues[z] + " in " + fieldName)
    if lyr.name == "MyFile":
        lyr.definitionQuery = fieldName + " =" + "'" + fieldValues[z] + "'"
    arcpy.CopyRows_management(lyr, filePath[z])
fin.close()

if spreadsheetType == "csv":
    FileTransformations.dbf2csv(outLocation, fieldValues, filePath)
elif spreadsheetType == "tsv":
    FileTransformations.dbf2tsv(outLocation, fieldValues, filePath)
