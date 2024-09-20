# -*- coding: cp936 -*-
import arcpy
from arcpy import env

env.workspace = "C:/instruction/"

raster1="C:/instruction/arcpy/data/data2/影像/采场.tif"
raster2="C:/instruction/arcpy/data/data2/影像/内排.tif"
raster3="C:/instruction/arcpy/data/data2/影像/外排.tif"
output_location="C:/instruction/arcpy/data/data2/结果/"
raster_dataset_name_with_extension="result2021.tif"
arcpy.MosaicToNewRaster_management([raster1,raster2,raster3], output_location,raster_dataset_name_with_extension, "#","16_BIT_UNSIGNED", "#", "4", "LAST","FIRST")