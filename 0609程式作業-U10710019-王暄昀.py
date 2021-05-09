#!/usr/bin/env python
# coding: utf-8

#Subject:0609作業
#Author:王暄昀
#Date:2020/06/21
#Description:將地震資料的CSV檔寫成pfile，用hypo3d讀出震央，將震央及測站位置利用GMT繪製在台灣地圖上。

import re
import math
import csv
import sys
import os
import struct
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from obspy import UTCDateTime, Stream, Trace

#讀取CSV檔
with open(r"D:\python\0609\PhaseNet-master\output\picks.csv") as fp:
    header = fp.readline()
    data = fp.readlines()

ddata = data[0]
ddata = ddata.strip()
#--------------------------------------------------------------
# 取得測站名稱及資料起始時間
tmp1 = ddata.split(",")[0]
sta = tmp1.split("-")[0]
yr = 2018
mo = 2
dy = 8
hr = 0
mn = 54
se = 0
segment = tmp1.split("-")[1]
#將時間設成檔名
pfname = f"{mo:02d}{dy:02d}{hr:02d}{mn:02d}.phn"
#將地震資料寫入pfname
with open(pfname,"w") as fp:   
#--------------------------------------------------------------
# 製作 Pfile 的 header
    header_str = f" {yr:4d}{mo:02d}{dy:02d}{hr:02d}{mn:02d}{se:02d}0.000000.0000000.00  0.00 0.0"
    fp.write(header_str+"\n")
#--------------------------------------------------------------
    for ddata in data:
        ddata = ddata.strip()
        P_sec=[]
        P_pro=[]
        S_sec=[]
        S_pro=[]
#--------------------------------------------------------------
# 取得測站名稱及資料起始時間
        tmp1 = ddata.split(",")[0]
        sta = tmp1.split("-")[0]
        yr = 2018
        mo = 2
        dy = 8
        hr = 0
        mn = 54
        se = 0
        segment = tmp1.split("-")[1]        
#--------------------------------------------------------------
# 取得 P 波到時 
        tmp1 = ddata.split(",")[1]
        if tmp1!="[]":
            tmp2 = tmp1.strip("[]").split()
        
            for i in tmp2:
                if segment==1:
                    P_sec.append(int( i.strip("[]") ) / 100.0 + int(se)+30)
                else:
                    P_sec.append(int( i.strip("[]") ) / 100.0 + int(se))
        else:
            P_sec=[0.00]
#--------------------------------------------------------------
# 取得 P 波到時機率
        tmp1 = ddata.split(",")[2]
        if tmp1!="[]":
            tmp2 = tmp1.strip("[]").split()
        
            for i in tmp2:
                P_pro.append( float( i ) )
        else:
            P_pro=[0.00]
#--------------------------------------------------------------    
# 取得 S 波到時 
        tmp1 = ddata.split(",")[3]
        if tmp1!="[]":
            tmp2 = tmp1.strip("[]").split()
        
            for i in tmp2:
                S_sec.append(int( i.strip("[]") ) / 100.0 + int(se))
        else:
            S_sec=[0.00]
#--------------------------------------------------------------
# 取得 S 波到時機率
        tmp1 = ddata.split(",")[4]
        if tmp1!="[]":
            tmp2 = tmp1.strip("[]").split()
            for i in tmp2:
                S_pro.append( float( i ) )
        else:
            S_pro=[0.00]
#--------------------------------------------------------------
        ss1 = f"{sta}-{yr}-{mo}-{dy}-{hr}-{mn}-{se}-{segment}"
        ss2 = f"{P_sec}-{P_pro}-{S_sec}-{S_pro}"
#--------------------------------------------------------------
# 製作 Pfile 的 station picking 資料
#    n=len(P_sec)
#    if n>1:
#        for i in range(n):
#            sta_pick = f" {sta:4s}    0.0   0   0  {mn:02d} {P_sec[i]:5.2f}  .00 0.00 {S_sec[i]:5.2f}  .00 0.00  .00  .00  .00  .00"
#            print(sta_pick)
#    else:
#        sta_pick = f" {sta:4s}    0.0   0   0  {mn:02d} {P_sec[0]:5.2f}  .00 0.00 {S_sec[0]:5.2f}  .00 0.00  .00  .00  .00  .00"
#        print(sta_pick)
        if P_sec[0]>0.0 and P_pro[0]>0.8:
            sta_pick = f" {sta:4s}   0.0   0   0  {mn:02d} {P_sec[0]:5.2f}  .00 0.00 {S_sec[0]:5.2f}  .00 0.00  .00  .00  .00  .00"
            fp.write(sta_pick+"\n")
#--------------------------------------------------------------
#利用hypo3d執行02080054檔案
os.system("hypo3d.exe 02080054.phn")
#定義函式unpackPfile
def unpackPfile(infile):
    #打開檔案
    with open(infile) as f:
        lines = f.readlines()
    #寫出時間
    tmp = lines[0]
    year = int(tmp[1:5])
    month = int(tmp[5:7])
    day = int(tmp[7:9])
    hour = int(tmp[9:11])
    minute = int(tmp[11:13])
    sec = float(tmp[13:19])
    #寫出經緯
    lat_d = float(tmp[19:21])
    lat_m = float(tmp[21:26])
    
    lon_d = float(tmp[26:29])
    lon_m = float(tmp[29:34])
    
    dep = float(tmp[34:40])

    dt = datetime(year,month,day,hour,minute,int(sec//1),int(sec%1 * 1000000))
    mag = float(tmp[40:44])
    
    pfile_info = {}
    pfile_info["ori_time"] = dt
    pfile_info["mag"] = mag
    pfile_info["lat"] = lat_d + lat_m/60.0
    pfile_info["lon"] = lon_d + lon_m/60.0
    pfile_info["dep"] = dep

    intensity = {}
    arrival_time = {}
    weighting = {}
    pga = {}
    for i in lines[1:]:
        sta = i[:5].strip() # strip 去掉左右空格
        weighting[sta] = int(float(i[35:39]))
        intensity[sta] = int(i[76:77])
        pga[sta] = float(i[78:83])
        arrival_time[sta] = pfile_info["ori_time"].replace(minute=int(i[21:23]),second=0,microsecond=0) + timedelta(seconds=float(i[23:29]))
    pfile_info["intensity"] = intensity
    pfile_info["arrival_time"] = arrival_time
    pfile_info["weighting"] = weighting
    pfile_info["pga"] = pga
    
    return pfile_info
#將檔案放入函式
data=unpackPfile("02080054.phn")
#將地震經緯度寫成txt檔
with open("E_lonlat.txt","w") as fp:
    ff=str(data["lon"])+","+str(data["lat"])
    fp.write(ff)
#開啟hypo3d.sta的測站資料並讀取
with open("c:\\datasrc\\hypo3d.sta","r") as fp:
    fp.readline()
    stalist=fp.readlines()
#建立字典將測站名稱及經緯寫入
stainfo={}
for i in stalist:
    i=i.strip()
    #print(i)

    lat_d = float(i[4:6])
    lat_m = float(i[6:11])
    lon_d = float(i[11:14])
    lon_m = float(i[14:19])

    lat = lat_d + lat_m/60.0
    lon = lon_d + lon_m/60.0
    sta = i.split()[-1]
    
    stainfo[sta]=[lon , lat]
#將測站經緯寫成txt檔
with open("lonlat.txt","w") as fp:
    for i in data["intensity"].keys():
        aa=str(stainfo[i]).strip("[]")+"\n"
        fp.write(aa)
#寫出一個bat檔，將lonlat.txt和E_lonlat.txt畫圖
with open("0609plot.bat","w") as fp:
    GMT=f"psbasemap -R119/123/21/26 -JM17.5 -Ba1f0.5 -P -K -V > 0609-U10710019.ps \n"
    fp.write(GMT)
    GMT=f"grdimage low_res_topo.grd -I+a2 -Ctopo2.cpt -JM -R  -K -O -V >> 0609-U10710019.ps \n"
    fp.write(GMT)        
    GMT=f"psxy TaiwanCounty.gmt -JM -R -W0.5  -K -O -V >> 0609-U10710019.ps \n"
    fp.write(GMT)
    GMT=f"psxy lonlat.txt -JM -R -St0.5 -W1 -G255/255/0  -K -O -V  >> 0609-U10710019.ps \n"
    fp.write(GMT)
    GMT=f"psxy E_lonlat.txt -JM -R -Sa0.6 -W1 -G255/0/0  -O -V >> 0609-U10710019.ps \n"
    fp.write(GMT)
    GMT=f"psconvert 0609-U10710019.ps \n"
    fp.write(GMT)
#執行bat檔
os.system("0609plot.bat")