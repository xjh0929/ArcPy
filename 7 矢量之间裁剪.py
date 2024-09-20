# -*- coding: cp936 -*-
import arcpy
from arcpy import env

# Set workspace
env.workspace = "C:/instruction/"

# Set local variables
in_features = "C:/instruction/arcpy/data/data7/ʸ��/2019_1.shp"
clip_features = "C:/instruction/arcpy/data/data7/ʸ��/ccbj_20210701_xw.shp"
out_feature_class ="C:/instruction/arcpy/data/data7/���/result.shp"
xy_tolerance = "#"

# Execute Clip
arcpy.Clip_analysis(in_features, clip_features, out_feature_class, xy_tolerance)
