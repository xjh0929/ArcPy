# -*- coding: cp936 -*-
import arcpy
# Set environment settings
arcpy.env.workspace = "C:/instruction/"
# Set local variables
in_table = "C:/instruction/arcpy/data/data6/矢量/采场.shp"
out_xls = "C:/instruction/arcpy/data/data6/结果/data.xls"
# Execute TableToExcel
arcpy.TableToExcel_conversion(in_table, out_xls)