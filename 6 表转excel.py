# -*- coding: cp936 -*-
import arcpy
# Set environment settings
arcpy.env.workspace = "C:/instruction/"
# Set local variables
in_table = "C:/instruction/arcpy/data/data6/ʸ��/�ɳ�.shp"
out_xls = "C:/instruction/arcpy/data/data6/���/data.xls"
# Execute TableToExcel
arcpy.TableToExcel_conversion(in_table, out_xls)