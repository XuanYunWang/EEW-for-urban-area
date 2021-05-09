#!/usr/bin/env python
# coding: utf-8

fp = open("nsta24.dat","r")
ss=fp.readlines()
fp.close()

fp = open("U10710019.txt","w")

for i in ss:
    res1=i.find("CWB")
    res2=i.find("FBA")
    res3=i.find("99999999")
    if res1 >-1 and res2>-1 and res3>-1:
        res1=i.split()
        lon=res1[1]
        lat=res1[2]
        print(i)
        print(lon,lat)
        tmp=str(lon)+" "+str(lat)+"\n"
        fp.write(tmp)
fp.close()
