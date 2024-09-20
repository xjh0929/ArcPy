# -*- coding: cp936 -*-
import arcpy
from arcpy import env

inRaster = "C:/instruction/arcpy/data/data3/影像/采场.tif"
outPoint = "C:/instruction/arcpy/data/data3/结果/采场.shp"
field = "VALUE"

# Execute RasterToPoint
arcpy.RasterToPoint_conversion(inRaster, outPoint, field)