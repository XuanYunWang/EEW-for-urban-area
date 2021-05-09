#!/usr/bin/env python
# coding: utf-8

#Subject:0602作業
#Author:王暄昀
#Date:2020/07/06
#Description:讀取地震資料，寫成CSV和npz。

from obspy import read, read_inventory
import numpy as np
import os
#讀取地震檔案
st1=read("2018-02-06-mww64-taiwan-2.miniseed")
#將資料寫成CSV檔
with open(r"D:\python\0602\PhaseNet-master\demo\fname.csv", 'w') as fp:
    fp.write("fname\n")
    for i in range(12):
        dd1=st1[0].data[3000*i:3000*(i+1)]*1.0
        dd2=st1[1].data[3000*i:3000*(i+1)]*1.0
        dd3=st1[2].data[3000*i:3000*(i+1)]*1.0
        dd=np.vstack((dd1,dd2,dd3)).T
        ffname = f"D:\\python\\0602\\PhaseNet-master\\demo\\dd{i}.npz"
        np.savez(ffname, data=dd)
        print(ffname)
        ffname = f"dd{i}.npz\n"
        fp.write(ffname)

