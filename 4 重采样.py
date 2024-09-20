# -*- coding: cp936 -*-
import arcpy
in_raster="C:/instruction/arcpy/data/data4/影像/Landsat_20210701_xw.tif"
out_raster="C:/instruction/arcpy/data/data4/结果/Landsat_20210701_xw.tif"
cell_size="0.0002"
arcpy.Resample_management(in_raster, out_raster, cell_size, "#")