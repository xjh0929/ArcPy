# -*- coding: cp936 -*-
import arcpy
from arcpy import env
env.workspace = "C:/instruction/"
from arcpy.sa import *
raster1="C:/instruction/arcpy/data/data5/影像/r_band.tif"
raster2="C:/instruction/arcpy/data/data5/影像/nir_band.tif"
output_raster="C:/instruction/arcpy/data/data5/结果/ndvi.tif"

expression=(Float(Raster(raster2))-Float(Raster(raster1)))/(Float(Raster(raster1))+Float(Raster(raster2)))
expression.save(output_raster)


