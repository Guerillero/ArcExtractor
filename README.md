ArcExtractor
============
This script extracts a dBase table (.dbf) for every instance of a value in a specific field. This is useful for moving data between ArcMap and an older program or if you need to move GIS data into several spreadsheets for analysis.

<h3>V. 0.1.0</h3>
To use, change `$FieldName` on line 61 to the field you want to extract by. Then create a text file matching the provided example. Finally, run the script ArcToolbox in ArcMap.

This was tested in ArcMap 10.2.1 and may not work with other versions of the software. Please let me know about any bugs.

<h3>Developmental version</h3>
The next version will contain its own ArcToolbox. The hope is that all the end user will need to provide is the list of fields.

<h3>Colophon</h3>
Special thanks to @MarkTraceur, @molly, and Stag for their help troublshooting my Python code.
