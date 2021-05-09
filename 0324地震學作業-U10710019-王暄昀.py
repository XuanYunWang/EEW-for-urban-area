#!/usr/bin/env python
# coding: utf-8

#Subject:0324地震學作業四
#Author:王暄昀
#Date: 2020/3/28
#Description:畫出S波的位移場

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 根據課本，S 波的位移場方程式 :  u(z,t) = (ikAy, -ikAx, 0) * exp(i(wt-kz))
# 這裡的 i 用 j 來表示 (因為python的虛部要用 j 表示)
# 方程式改寫成 :　u(z,t) = (jkAy, -jkAx, 0) * exp(j(wt-kz))
# 方程式改寫成 :　u(z,t) = (jkAy, -jkAx, 0) *( cos(wt-kz)+jsin(wt-kz) ) 
# 方程式改寫成 :　u(z,t) = (jkAy*( cos(wt-kz)+jsin(wt-kz) ), (-jkAx*( cos(wt-kz)+jsin(wt-kz) )), 0)
# 方程式改寫成 :　u(z,t) = (jkAy* cos(wt-kz)-kAy*sin(wt-kz) ), (-jkAx*cos(wt-kz)+kAx*sin(wt-kz) )), 0)
# 取實部 :
# u(z,t) = ( -kAy*sin(wt-kz) , kAx*sin(wt-kz) , 0 )

#P波
# u1(z,t)=(0,0,-jkAz) *( cos(wt-kz)+jsin(wt-kz) )
# u1(z,t)=jkAz*( 0,0,cos(wt-kz)+jsin(wt-kz))
#取實部
# u1(z,t)=(0,0,kAz*sin(wt-kz))

# u,u1 是隨 z 軸 及時間 t 而變化的位移量
# k 是 wave number
# w 是角頻率
# Ay 是 Y 方向振幅， Ax 是 x 方向振幅

#S波
# ( -kAy*sin(wt-kz) , kAy*sin(wt-kz) , 0 ) 代表  (x, y, z) 3個分量
# 這個方程式可以從 3 個軸來看
# x 軸: u(z,t)= -kAy*sin(wt-kz)
# y 軸: u(z,t)= kAy*sin(wt-kz)
# z 軸: u(z,t)= 0,在z軸上沒有位移

# S 波的位移場為 :

# 考慮在 x 軸上位移 
# x 軸: u(z,t)= -kAy*sin(wt-kz) .... 用python改寫如下 :
# x = -k*Ay*np.sin(w*t-k*z)

# 考慮在 y 軸上位移 
# y 軸: u(z,t)= kAx*sin(wt-kz) .... 用python改寫如下 :
# y = k*Ax*np.sin(w*t-k*z)

# 固定 t 改變 z 來作圖 ----> 代表在某一個瞬間眼看到的波形在空間中的變化
# 假設一些初始値

#P波
# ( 0,0, kAy*sin(wt-kz) ) 代表  (x, y, z) 3個分量
# 這個方程式可以從 3 個軸來看
# x 軸: u1(z,t)= 0,在x軸上沒有位移
# y 軸: u1(z,t)= 0,在y軸上沒有位移
# z 軸: u1(z,t)= -kAzsin(wt-kz)

# P 波的位移場為 :

# 考慮在 z 軸上位移 
# z 軸: u1(z,t)= -kAyzsin(wt-kz) .... 用python改寫如下 :
# z = -k*Ay*np.sin(w*t-k*z)

Ax = 2
Ay = 2
t = 1
#z軸範圍從0到8每0.2畫一個點
z = np.arange(0,8,0.2)
# 假設波長為 2 ， 由於 k*lamda = 2*pi ， 將 lamda = 2 代入 ， 得到  k = pi
# 假設週期為 0.8 ， 由於 w*T = 2*pi ， 將 T = 0.8 代入 ， 得到  w = 2.5pi
lamda = 2
k = 2*np.pi / lamda

period = 0.8
w = 2*np.pi / period

#畫出t從1-9的圖,每一秒畫一張
for t in np.arange(1,10,1):
    fig = plt.figure()
    ax = Axes3D(fig)
    x = -k*Ax*np.sin(w*t-k*z)
    
    #波的範圍從-40到40,每10畫一條線
    for i in np.arange(-40,41,10):  
        ax.scatter(z, y+i, x+i, marker="o")

    ax.set_xlabel('Z Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('X Label')
    #旋轉圖片
    ax.view_init(20, 100)
    
    fname = f"pic{t}.jpg"
    plt.savefig(fname)
   
#P波
Az = 2
t = 1
#z軸範圍從0到8每0.2畫一個點
x = np.arange(0,8,0.2)
# 假設波長為 2 ， 由於 k*lamda = 2*pi ， 將 lamda = 2 代入 ， 得到  k = pi
# 假設週期為 0.8 ， 由於 w*T = 2*pi ， 將 T = 0.8 代入 ， 得到  w = 2.5pi
lamda = 2
k = 2*np.pi / lamda

period = 0.8
w = 2*np.pi / period

#畫出t從1-9的圖,每一秒畫一張
for t in np.arange(1,10,1):
    fig = plt.figure()
    ax = Axes3D(fig)
    x = -k*Ax*np.sin(w*t-k*z)
    
    #波的範圍從-40到40,每10畫一條線
    for i in np.arange(-40,41,10):  
        ax.scatter(z+i, y, x, marker="o")

    ax.set_xlabel('Z Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('X Label')
    #旋轉圖片
    ax.view_init(20, 100)
    
    fname = f"pic{t}.jpg"
    plt.savefig(fname)