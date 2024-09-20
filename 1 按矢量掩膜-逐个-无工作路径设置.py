# -*- coding: cp936 -*-
import arcpy
from arcpy import env
from arcpy.sa import *

in_raster="C:/instruction/arcpy/data/data1/影像/Landsat_20160701_xw.tif"
in_mask_data="C:/instruction/arcpy/data/data1/矢量/ccbj_20160701_xw.shp"
out_raster="C:/instruction/arcpy/data/data1/结果/result2016.tif"

outExtractByMask = ExtractByMask(in_raster, in_mask_data)
outExtractByMask.save(out_raster)