# -*- coding: cp936 -*- #这是一种简体中文的编码格式，用于正确处理脚本中的中文字符。
import arcpy
from arcpy import env ###用于设置工作环境的参数，例如工作空间和输出坐标系统等。
from arcpy.sa import *  #从 arcpy.sa 模块（Spatial Analyst 工具）中导入所有工具，这些工具主要用于栅格数据的空间分析。

for year in [2016,2017,2018,2019,2020,2021]:
    in_raster="C:/instruction/arcpy/data/data1/影像/Landsat_"+str(year)+"0701_xw.tif"
    in_mask_data="C:/instruction/arcpy/data/data1/矢量/ccbj_"+str(year)+"0701_xw.shp"
    out_raster="C:/instruction/arcpy/data/data1/结果/result"+str(year)+".tif"

    outExtractByMask = ExtractByMask(in_raster, in_mask_data)
    outExtractByMask.save(out_raster)