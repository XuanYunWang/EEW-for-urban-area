#!/usr/bin/env python
# coding: utf-8

# In[32]:


#Subject:0303作業一
#Author:王暄昀
#Date:2020/03/07
#Description:計算文章中每個出現單字的頻率並排序


# In[33]:


#輸入Data
a="This book is an introduction to seismology, the study of elastic waves or sound waves in the solid earth. Conceptually, the subject is simple. Seismic waves are generated at a source, which can be natural, such as an earthquake, or artificial, such as an explosion. The resulting waves propagate through the medium, some portion of the earth, and are recorded at a receiver (Fig. 1.1-1). A seismogram, the record of the motion of the ground at a receiver called a seismometer, thus contains information about both the source and the medium. This information can take several forms. The waves provide information on the location and nature of the source that generated them. If the origin time when the waves left the source is known, their arrival time at the receiver gives the travel time required to pass through the medium, and hence information about the speed at which they traveled, and thus the physical properties of the medium. In addition, because the amplitude and shape of the wave pulses that left the source are affected by propagation through the medium, the signals observed on seismograms provide additional information about the medium."
#轉成小寫
aa=a.lower()


# In[34]:


#以空格隔開資料
aa_list = aa.split()
#去掉,和.
for item in aa.split():
    if item[-1]==',' or item[-1]=='.':
        aa_list.remove(item)
        aa_list.append(item[0:-1])


# In[35]:


#去掉重複的字
aa_set = set(aa_list)


# In[36]:


#利用串列生成式寫出aa1，表示字與字的數量
aa1=[(aa_list.count(i),i) for i in aa_set]


# In[38]:


#按照字的數量由多到少排列(True為降序)
aa2=sorted(aa1, reverse=True)


# In[40]:


print(aa2)

