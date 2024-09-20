# -*- coding: cp936 -*-
import arcpy
from arcpy.sa import *

# ���Spatial Analyst��չ���
arcpy.CheckOutExtension("Spatial")

# �������4�����ε�Ӱ��ľ���·��
input_image_path = "C:/instruction/arcpy/data/data5/Ӱ��/Landsat_20210701_xw.tif"

# ���NDVIӰ��ľ���·��
ndvi_output_path = "C:/instruction/arcpy/data/data5/���/Landsat_ndvi.tif"

# ��ȡ��ɫ���� (����������) �ͽ����Ⲩ�� (���ĸ�����)
red_band = Raster(input_image_path + r"\Band_3") * 1.0
nir_band = Raster(input_image_path + r"\Band_4") * 1.0

# ����NDVI (NDVI = (NIR - Red) / (NIR + Red))
ndvi = (nir_band - red_band) / (nir_band + red_band)

# ����NDVI���
ndvi.save(ndvi_output_path)

# �ͷ�Spatial Analyst��չ���
arcpy.CheckInExtension("Spatial")

# print(f"NDVI������ɣ�����ѱ���Ϊ: {ndvi_output_path}")


