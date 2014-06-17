##################################################
# Extract a dbtable for every UID in a geo-file  #
# Written by Thomas Fish                         #
# Released under the MIT License                 #
##################################################

#Start dependency tree
import arcpy
from arcpy import env

#declare map
mxd = arcpy.mapping.MapDocument("CURRENT")


#Import data from ArcMap
fileToConvert = arcpy.GetParameterAsText(0)
listUID = arcpy.GetParameterAsText(1)
outLocation = arcpy.GetParameterAsText(2)

#translate file into layer
lyr = arcpy.mapping.Layer(fileToConvert)
lyr.name = "MyFile"
###arcpy.MakeTableView_management (fileToConvert, "tableNew")
#declare array for UIDs
UID = []

#declare the file to open
fin = open (listUID)

#tell end user if there is an error
if fin.closed:
	arcpy.AddMessage("File failed to open")

for line in fin:
	#Turn each line in the file into an entry to the array
	lineClear = str.strip ( line )
	UID.append(lineClear)
 
#declare array for file names

fileName = []

#make file names from UIDs
for i in range (len(UID)):
        fileName.append (UID[i] + ".dbf")

filePath = []

for y in range (len(fileName)):
        filePath.append(outLocation + "\\" + fileName[y])

#test file names
for x in range (len(fileName)):
        arcpy.AddMessage(UID [x] + ", " + filePath[x])

for z in range (len(UID)):
	#Extract out only the entries that are wanted 
    arcpy.AddMessage("enter final for loop")
    if lyr.name == "MyFile": 
        lyr.definitionQuery = "client_id =" + "'" + UID[z] + "'"
        arcpy.AddMessage("narrow data")
	#Convert the table into a dbf
	arcpy.AddMessage("Converting UID " + UID[z])
	#Error is here
	arcpy.CopyRows_management(lyr, filePath[z])
