# extentupdate.py
# Update geographic extent for location inset maps for survey points database
# Kevin Alexander, Karen Brandt
# 3-21-2012
# 9-23-2012 add comment line here to test github

import arcpy

#Create a update cursor from the ExtentAreas featureclass

inputFile = "\\\\ccb-fs-01\\ITdept\\GIS\\Interns\\KALEXANDER\\Broomfield_Survey_Points.gdb\\ExtentAreas"

urows = arcpy.UpdateCursor(inputFile, "", "", "", "")

#use for loop to update all the rows

for urow in urows:

    geom = urow.shape
    ext = geom.extent  # or row.Shape.extent
    
# to check that the script is working

    print "Starting Update"
    
# update the EXTENT_IMAGE field

    urow.EXTENT_IMAGE = str(ext.XMin) + " " + str(ext.YMin)+ " " + str(ext.XMax) + " " + str(ext.YMax)
    urows.updateRow(urow)

# to check that the script is working
    print str(ext.XMin) + " " + str(ext.YMin)+ " " + str(ext.XMax) + " " + str(ext.YMax)

                                                                   
