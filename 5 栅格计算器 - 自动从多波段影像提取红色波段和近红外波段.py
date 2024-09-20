# -*- coding: cp936 -*-
import arcpy
from arcpy.sa import *

# 检查Spatial Analyst扩展许可
arcpy.CheckOutExtension("Spatial")

# 输入包含4个波段的影像的绝对路径
input_image_path = "C:/instruction/arcpy/data/data5/影像/Landsat_20210701_xw.tif"

# 输出NDVI影像的绝对路径
ndvi_output_path = "C:/instruction/arcpy/data/data5/结果/Landsat_ndvi.tif"

# 提取红色波段 (第三个波段) 和近红外波段 (第四个波段)
red_band = Raster(input_image_path + r"\Band_3") * 1.0
nir_band = Raster(input_image_path + r"\Band_4") * 1.0

# 计算NDVI (NDVI = (NIR - Red) / (NIR + Red))
ndvi = (nir_band - red_band) / (nir_band + red_band)

# 保存NDVI结果
ndvi.save(ndvi_output_path)

# 释放Spatial Analyst扩展许可
arcpy.CheckInExtension("Spatial")

# print(f"NDVI计算完成，结果已保存为: {ndvi_output_path}")


