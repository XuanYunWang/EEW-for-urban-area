#!/usr/bin/env python
# coding: utf-8

#Subject:0331作業
#Author:王暄昀
#Date:2020/04/01
#Description:分別取出儀器停用時間為99999999、儀器所屬單位為CWB、儀器種類為FBA的測站，以及儀器停用時間為99999999、儀器所屬單位為IES、儀器種類為BB的測站，位置以及數量，並畫圖。

fp = open("nsta24.dat","r")
ss=fp.readlines()
fp.close()

y=[]
fp = open("U10710019.Y.txt","w")

for i in ss:
    res1=i.find("CWB")
    res2=i.find("FBA")
    res3=i.find("99999999")
    if res1 >-1 and res2>-1 and res3>-1:
        res1=i.split()
        lon=res1[1]
        lat=res1[2]
        tmp=str(lon)+" "+str(lat)
        tmp1=str(lon)+" "+str(lat)+"\n"
        y.append(tmp)
        fp.write(tmp1)
fp.close()

r=[]
fp = open("U10710019.R.txt","w")

for i in ss:
    res1=i.find("IES")
    res2=i.find("BB")
    res3=i.find("99999999")
    if res1 >-1 and res2>-1 and res3>-1:
        res1=i.split()
        lon=res1[1]
        lat=res1[2]
        tmp=str(lon)+" "+str(lat)
        tmp1=str(lon)+" "+str(lat)+"\n"
        r.append(tmp)
        fp.write(tmp1)
fp.close()

print("儀器停用時間為99999999，儀器所屬單位為CWB，儀器種類為FBA的測站數量為:"+str(len(y)))
print("儀器停用時間為99999999，儀器所屬單位為IES，儀器種類為BB的測站數量為:"+str(len(r)))