# -*- coding: cp936 -*-
import arcpy
from arcpy import env

env.workspace = "C:/instruction/"

raster1="C:/instruction/arcpy/data/data2/Ӱ��/�ɳ�.tif"
raster2="C:/instruction/arcpy/data/data2/Ӱ��/����.tif"
raster3="C:/instruction/arcpy/data/data2/Ӱ��/����.tif"
output_location="C:/instruction/arcpy/data/data2/���/"
raster_dataset_name_with_extension="result2021.tif"
arcpy.MosaicToNewRaster_management([raster1,raster2,raster3], output_location,raster_dataset_name_with_extension, "#","16_BIT_UNSIGNED", "#", "4", "LAST","FIRST")