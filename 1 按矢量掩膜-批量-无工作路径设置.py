# -*- coding: cp936 -*- #����һ�ּ������ĵı����ʽ��������ȷ����ű��е������ַ���
import arcpy
from arcpy import env ###�������ù��������Ĳ��������繤���ռ���������ϵͳ�ȡ�
from arcpy.sa import *  #�� arcpy.sa ģ�飨Spatial Analyst ���ߣ��е������й��ߣ���Щ������Ҫ����դ�����ݵĿռ������

for year in [2016,2017,2018,2019,2020,2021]:
    in_raster="C:/instruction/arcpy/data/data1/Ӱ��/Landsat_"+str(year)+"0701_xw.tif"
    in_mask_data="C:/instruction/arcpy/data/data1/ʸ��/ccbj_"+str(year)+"0701_xw.shp"
    out_raster="C:/instruction/arcpy/data/data1/���/result"+str(year)+".tif"

    outExtractByMask = ExtractByMask(in_raster, in_mask_data)
    outExtractByMask.save(out_raster)