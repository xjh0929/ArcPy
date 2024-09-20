# -*- coding: cp936 -*-
import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = "C:/instruction/arcpy/data/data1/"

in_raster="Ӱ��/Landsat_20160701_xw.tif"
in_mask_data="ʸ��/ccbj_20160701_xw.shp"
out_raster="result2016.tif"

outExtractByMask = ExtractByMask(in_raster, in_mask_data)
outExtractByMask.save(out_raster)