#!/usr/bin/env python
# coding: utf-8

#Subject:0317作業二
#Author:王暄昀
#Date:2020/03/22
#Description:取出nth為3,mark為230的地震，並用GMT畫出震央分布圖。


import pandas as pd 
import matplotlib.pyplot as plt
#打開地震資料，將資料存成list，再關閉檔案
fp = open("EEW_2018_cwb24_mpd.txt")
data=fp.readlines()
fp.close()
#新增一個list為n_data，用for迴圈和if迴圈取出mark=230,nth=3的地震，再加入n_data
n_data=[]
flag=0
index = 0
for i in data:
    if "ttt" in i:
        flag = 1       
        index = index + 1
        event_num = i.split()[-1].split("_")[0]
    if "230" in i and flag==1:
        if "3 Mpd" in i:
            flag=0

            i.split()
            mag = i.split()[5]
            lat = i.split()[6]
            lon = i.split()[7]
            dep = i.split()[8]
            nsta = i.split()[9]
            gap = i.split()[-4]
    
            aa = f"{index} 3 {mag} {lon} {lat} {dep} {nsta} {gap} 230 {event_num}"
            n_data.append(aa)
#利用串列生成式寫出將n_data以空格分隔的n_data_list
n_data_list=[i.split() for i in n_data]
#將n_data_list轉為pandas並將欄位取名
cn=["index","nth","mag","lon","lat","dep","nsta","gap","mark","no"]
off_data = pd.DataFrame(n_data_list,columns=cn,dtype="float")
#取出off_data中經緯度資料並轉成list
aaa=off_data.loc[:119,"lon":"lat"]
a1=aaa.values.tolist()
#新增一個txt檔，以for迴圈將經緯度資料寫入檔案，再關閉檔案
fp = open('0317-U10710019.txt','w');
for i in a1:
    k=str(i[0])+" "+str(i[1])+"\n"
    fp.write(k)

fp.close()