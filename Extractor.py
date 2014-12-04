##################################################################
# Extract a dbtable for every instance of a value in a geo-file  #
# Written by Thomas Fish                                         #
# Released under the MIT License                                 #
#                                                                #
#                 FOR ARCMAP 10.X ONLY                           # 
##################################################################

#Start dependency tree
import arcpy
from arcpy import env

#declare map
mxd = arcpy.mapping.MapDocument("CURRENT")


#Import data from ArcMap
fileToConvert = arcpy.GetParameterAsText(0)
listFieldValues = arcpy.GetParameterAsText(1)
outLocation = arcpy.GetParameterAsText(2)
fieldName = arcpy.GetParameterAsText(3)
#future place for field on what type of table to end up as
spreadsheetType = arcpy.GetParameterAsText(4)

if spreadsheetType == "dbf":
	fileType = ".dbf"
else if spreadsheetType == "csv":
	fileType = ".txt"
else if spreadsheetType == "txt":
	fileType = ".txt"
else
	arcpy.AddMessage("ERROR: Not a valid file type")

#translate file into layer
lyr = arcpy.mapping.Layer(fileToConvert)
lyr.name = "MyFile"

#declare array for UIDs
fieldValues = []

#declare the file to open
fin = open (listFieldValues)

#tell end user if there is an error
if fin.closed:
	arcpy.AddMessage("ERROR: File failed to open")

for line in fin:
	#Turn each line in the file into an entry to the array
	lineClear = str.strip ( line )
	fieldValues.append(lineClear)

#declare array for file names

fileName = []

#make file names from UIDs
for i in range (len(fieldValues)):
        fileName.append (fieldValues[i] + "fileType")

filePath = []

for y in range (len(fileName)):
        filePath.append(outLocation + "\\" + fileName[y])

for z in range (len(fieldValues)):
	#Extract out only the entries that are wanted 
    arcpy.AddMessage("Currently extracting "+ fieldValues[z] + " in " + fieldName)
    if lyr.name == "MyFile": 
        lyr.definitionQuery = fieldName + " =" + "'" + fieldValues[z] + "'"
	arcpy.CopyRows_management(lyr, filePath[z])

