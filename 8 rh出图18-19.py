# -*- coding: cp936 -*-
import arcpy
from arcpy import env
from arcpy.sa import *
import time
import os
import arcpy.mapping as map

tiffolder="C:/instruction/arcpy/data/data8/rh/" ###���tif�ļ���
ccfolder="C:/instruction/arcpy/data/data8/ʸ��/" ###���tif�ļ���
wpfolder="C:/instruction/arcpy/data/data8/ʸ��/" ###���tif�ļ���
npfolder="C:/instruction/arcpy/data/data8/ʸ��/" ###���tif�ļ���
kqfolder="C:/instruction/arcpy/data/data8/ʸ��/" ###���tif�ļ���
outfolder="C:/instruction/arcpy/data/data8/pic/"

tiflist=os.listdir(tiffolder)
mxd=map.MapDocument("C:/instruction/arcpy/data/data8/rh.mxd") ##mxd
for tiffile in tiflist:
    if tiffile.endswith(".tif"):
        frame = map.ListDataFrames(mxd)
        lyr = map.ListLayers(mxd)
        elm = map.ListLayoutElements(mxd, "TEXT_ELEMENT","name")
        elm[0].text = tiffile.split("_")[1][0:4]+"��"+tiffile.split("_")[1][5:6]+"��"

        elm2 = map.ListLayoutElements(mxd, "TEXT_ELEMENT", "name2")
        elm2[0].text = "���ʪ��"+tiffile.split("_")[1][0:4] + "��"


        lyr[0].replaceDataSource(npfolder, "SHAPEFILE_WORKSPACE", "npbj_" + tiffile.split("_")[1][0:4] + "0701_xw")
        lyr[1].replaceDataSource(wpfolder,"SHAPEFILE_WORKSPACE", "wpbj_"+tiffile.split("_")[1][0:4]+"0701_xw")
        lyr[2].replaceDataSource(ccfolder, "SHAPEFILE_WORKSPACE", "ccbj_"+tiffile.split("_")[1][0:4]+"0701_xw")
        lyr[3].replaceDataSource(kqfolder, "SHAPEFILE_WORKSPACE", "boundary_20210701_xw")
        lyr[4].replaceDataSource(tiffolder, "RASTER_WORKSPACE", tiffile.split(".tif")[0])
    #
        arcpy.RefreshActiveView()
        map.ExportToJPEG(mxd,outfolder+tiffile.split(".tif")[0]+".jpg",resolution=75)
    # else:
    #     pass
