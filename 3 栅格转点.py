# -*- coding: cp936 -*-
import arcpy
from arcpy import env

inRaster = "C:/instruction/arcpy/data/data3/Ӱ��/�ɳ�.tif"
outPoint = "C:/instruction/arcpy/data/data3/���/�ɳ�.shp"
field = "VALUE"

# Execute RasterToPoint
arcpy.RasterToPoint_conversion(inRaster, outPoint, field)