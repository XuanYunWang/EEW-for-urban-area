#!/usr/bin/env python
# coding: utf-8

#Subject:0414作業
#Author:王暄昀
#Date:2020/05/02
#Description:算出測站的Back_Azimuth，取出測站及地震波資料，轉成ZRT方向，利用GMT畫出波形再討論。

from obspy import read, read_inventory
import numpy as np
import pandas as pd 
import os

#算出測站的Back_Azimuth
colatE = 90-(-60.3783)
lonE = -46.5876
colatS = 90-29.33
lonS = -103.67

X = np.cos(colatE*np.pi/180)*np.cos(colatS*np.pi/180)+np.sin(colatE*np.pi/180)*np.sin(colatS*np.pi/180)*np.cos((lonS-lonE)*np.pi/180)
Delta = np.arccos(X) * 180/np.pi

YY = np.sin(colatS*np.pi/180)*np.sin((lonS-lonE)*np.pi/180)
XX = np.cos(colatS*np.pi/180)*np.sin(colatE*np.pi/180)-np.sin(colatS*np.pi/180)*np.cos(colatE*np.pi/180)*np.cos((lonS-lonE)*np.pi/180)
Azimuth = np.arctan(YY/XX) * 180 / np.pi

YY = np.sin(colatE*np.pi/180)*np.sin((lonE-lonS)*np.pi/180)
XX = np.cos(colatE*np.pi/180)*np.sin(colatS*np.pi/180)-np.sin(colatE*np.pi/180)*np.cos(colatS*np.pi/180)*np.cos((lonE-lonS)*np.pi/180)
Back_Azimuth = np.arctan(YY/XX) * 180 / np.pi + 180

#取出測站及地震波資料
st1 = read("2013-11-17-mw78-scotia-sea.miniseed",format="MSEED")
inv = read_inventory("fdsn-station_2020-04-21T04_26_12.xml")


#將ZNE的資料放進pandas
plotE=st1[0]
plotN=st1[1]
plotZ=st1[2]
x = np.arange(0,len(plotZ.data))/plotZ.stats.sampling_rate
#因為Z方向資料少一筆，所以另外兩個少取一筆資料
data=np.vstack((x,plotE.data[0:218400],plotN.data[0:218400],plotZ.data)).T
aa = pd.DataFrame(data,columns=["x","EW","NS","vertical"])

#將ZNE的資料儲存成txt檔
aa[["x","EW"]].to_csv("plotE.txt",sep=" ",header=None, index=None)
aa[["x","NS"]].to_csv("plotN.txt",sep=" ",header=None, index=None)
aa[["x","vertical"]].to_csv("plotZ.txt",sep=" ",header=None, index=None)

#寫出bat檔繪製ZNE的地震波圖(打開bat檔依序寫入ZNE方向的地震波)
with open("plot.bat","w") as fp:
    
    Xmin = aa.x.min()
    Xmax = aa.x.max()
    X_space = ( aa.x.max() - aa.x.min() )/10
    Y_size = 5    
    
    Ymin = aa.vertical.min()
    Ymax = aa.vertical.max()
    Y_space = int(( aa.vertical.max() - aa.vertical.min() )/5)
    GMT = f"psxy plotZ.txt -JX25/{Y_size} -R{Xmin}/{Xmax}/{Ymin}/{Ymax} -B{X_space}/{Y_space}WESn -W1 -V -K > plotZNE-U10710019.ps \n"
    fp.write(GMT)
    GMT = f"echo {X_space*0.5}  {Y_space*1.8}  Z > legend-ZNE.txt \n"
    fp.write(GMT)
    GMT = f"pstext legend-ZNE.txt -JX -R -B -V -K -O >> plotZNE-U10710019.ps \n"
    fp.write(GMT)
  
    Ymin = aa.NS.min()
    Ymax = aa.NS.max()
    Y_space = int(( aa.NS.max() - aa.NS.min() )/5)
    GMT = f"psxy plotN.txt -JX25/{Y_size} -R{Xmin}/{Xmax}/{Ymin}/{Ymax} -B{X_space}/{Y_space}WEsn -W1 -V -Y{Y_size+0.5} -K -O >> plotZNE-U10710019.ps \n"
    fp.write(GMT)
    GMT = f"echo {X_space*0.5}  {Y_space*1.8} N > legend-ZNE.txt \n"
    fp.write(GMT)
    GMT = f"pstext legend-ZNE.txt -JX -R -B -V -K -O >> plotZNE-U10710019.ps \n"
    fp.write(GMT)
    
    Ymin = aa.EW.min()
    Ymax = aa.EW.max()    
    Y_space = int(( aa.EW.max() - aa.EW.min() )/5)
    GMT = f"psxy plotE.txt -JX25/{Y_size} -R{Xmin}/{Xmax}/{Ymin}/{Ymax} -B{X_space}/{Y_space}WEsn -W1 -V -Y{Y_size+0.5} -K -O >> plotZNE-U10710019.ps \n"
    fp.write(GMT)
    GMT = f"echo {X_space*0.5}  {Y_space*1.8}  E > legend.txt \n"
    fp.write(GMT)
    GMT = f"pstext legend.txt -JX -R -B -V -O >> plotZNE-U10710019.ps \n"
    fp.write(GMT)
    
    fp.write("psconvert plotZNE-U10710019.ps \n")
    fp.write("plotZNE-U10710019.jpg")

#將ZNE的資料轉換ZRT的資料
st2=st1.rotate(method="NE->RT", inventory=inv, back_azimuth=154.99143292771993) 

#將ZRT的資料放進pandas
transverse = st2[0]
radial = st2[1]
vertical = st2[2]
x = np.arange(0,len(vertical.data))/vertical.stats.sampling_rate
#因為Z方向資料少一筆，所以另外兩個少取一筆資料
data=np.vstack((x,radial.data[0:218400],transverse.data[0:218400],vertical.data)).T
dd = pd.DataFrame(data,columns=["x","radial","transverse","vertical"])

#將ZRT的資料儲存成txt檔 
dd[["x","radial"]].to_csv("radial.txt",sep=" ",header=None, index=None)
dd[["x","transverse"]].to_csv("transverse.txt",sep=" ",header=None, index=None)
dd[["x","vertical"]].to_csv("vertical.txt",sep=" ",header=None, index=None)

#寫出bat檔繪製ZRT的地震波圖(打開bat檔依序寫入ZRT方向的地震波)
with open("plot_surface_wave.bat","w") as fp:
    
    Xmin = dd.x.min()
    Xmax = dd.x.max()
    X_space = ( dd.x.max() - dd.x.min() )/10
    Y_size = 5
    
    Ymin = dd.vertical.min()
    Ymax = dd.vertical.max()
    Y_space = int(( dd.vertical.max() - dd.vertical.min() )/5)
    GMT = f"psxy vertical.txt -JX25/{Y_size} -R{Xmin}/{Xmax}/{Ymin}/{Ymax} -B{X_space}/{Y_space}WESn -W1 -V -K > plotZRT-U10710019.ps \n"
    fp.write(GMT)
    GMT = f"echo {X_space*0.5}  {Y_space*1.8}  Vertical > legend.txt \n"
    fp.write(GMT)
    GMT = f"pstext legend.txt -JX -R -B -V -K -O >> plotZRT-U10710019.ps \n"
    fp.write(GMT)
    
    Ymin = dd.transverse.min()
    Ymax = dd.transverse.max()    
    Y_space = int(( dd.transverse.max() - dd.transverse.min() )/5)
    GMT = f"psxy transverse.txt -JX25/{Y_size} -R{Xmin}/{Xmax}/{Ymin}/{Ymax} -B{X_space}/{Y_space}WEsn -W1 -V -Y{Y_size+0.5} -K -O >> plotZRT-U10710019.ps \n"
    fp.write(GMT)
    GMT = f"echo {X_space*0.5}  {Y_space*1.8}  Transverse > legend.txt \n"
    fp.write(GMT)
    GMT = f"pstext legend.txt -JX -R -B -V -K -O >> plotZRT-U10710019.ps \n"
    fp.write(GMT)
    
    Ymin = dd.radial.min()
    Ymax = dd.radial.max()    
    Y_space = int(( dd.radial.max() - dd.radial.min() )/5)
    GMT = f"psxy radial.txt -JX25/{Y_size} -R{Xmin}/{Xmax}/{Ymin}/{Ymax} -B{X_space}/{Y_space}WEsn -W1 -V -Y{Y_size+0.5} -K -O >> plotZRT-U10710019.ps \n"
    fp.write(GMT)
    GMT = f"echo {X_space*0.5}  {Y_space*1.8}  Radial > legend.txt \n"
    fp.write(GMT)
    GMT = f"pstext legend.txt -JX -R -B -V -O >> plotZRT-U10710019.ps \n"
    fp.write(GMT)
    
    fp.write("psconvert plotZRT-U10710019.ps \n")
    fp.write("plotZRT-U10710019.jpg")

#執行bat檔
os.system("plot.bat")
os.system("plot_surface_wave.bat")