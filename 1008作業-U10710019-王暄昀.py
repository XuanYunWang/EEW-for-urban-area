#!/usr/bin/env python
# coding: utf-8

# In[63]:


fp = open("bookinfo_1.txt","r")
a=fp.readline()
b=fp.readline()
c=fp.readline()
fp.close()


# In[64]:


a=a.rstrip()
name = a.split(",")
b=b.rstrip()
number = b.split(",")
c=c.rstrip()
price = c.split(",")


# In[65]:


User_input = "Y"


while (User_input=="Y" or User_input=="y"):
    print("----------------------------")
    print("1. Input Data  :")
    print("2. Show Data   :")
    print("3. Delete Data :")
    print("4. Inquiry Data:")
    print("5. Quit.")
    print("----------------------------")
    choice = input("Please select a choice:")
    print("----------------------------")
    print("Your choice is {}. ".format(choice))
    if choice=='1':
        print("--新增資料--")
        name.append(input("請輸入書名 : "))
        number.append(input("請輸入編號 : "))
        price.append( int(input("請輸入價錢 : ")) )
    elif choice=='2':
        print("--顯示資料--")
        for index in range(0,len(name)):
            print("No.%03d, 書名 :%10s, 編號 :%5s, 價錢 :%10s"%(index+1,name[index],number[index],price[index]))
    elif choice=='3':
        print("--刪除資料--")
        r_name=input("請輸入想要刪除的書名 : ")
        if r_name in name:
            pos=name.index(r_name)
            name.remove(name[pos])
            price.remove(price[pos])
            number.remove(number[pos])
    elif choice=='4':
        print("---------------")
        print("1.利用書名查詢")
        print("2.利用編號查詢")
        print("---------------")
        choice = input("Please select a choice:")
        print("---------------")
        print("Your choice is {}. ".format(choice))
        if choice=='1':
            in_name=input("請輸入書名 : ")
            if in_name in name:
                pos=name.index(in_name)
                print("No.%03d, 書名 :%10s, 編號 :%5s, 價錢 :%10d"%(pos+1,name[pos],number[pos],price[pos]))
            if not in_name in name:
                print("----------------------------")
                print("很抱歉查無此書!請重新輸入")
        elif choice=='2':
            in_number=input("請輸入編號 : ")
            if in_number in number:
                pos=number.index(in_number)
                print("No.%03d, 書名 :%10s, 編號 :%5s, 價錢 :%10d"%(pos+1,name[pos],number[pos],price[pos]))
            if not in_number in number:
                print("----------------------------")
                print("很抱歉查無此書!請重新輸入")
        
    elif choice=='5':        
        User_input = "N"
        print("程式結束 !")


# In[66]:


fp = open("bookinfo_2.txt","w")
for i in range(3):
    if i ==2:
        fp.write(name[i]+"\n")
    else:
        fp.write(name[i]+",")
for i in range(3):
    if i ==2:
        fp.write(number[i]+"\n")
    else:
        fp.write(number[i]+",")
for i in range(3):
    if i ==2:
        fp.write(price[i])
    else:
        fp.write(price[i]+",")
fp.close()


# In[67]:


def function_sum(price):
    ans=0
    for i in price:
        ans=int(ans)+int(i)
        
    return ans


# In[68]:


function_sum(price)


# In[70]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

price = [1280,5000,260]
name = ["Math","Physics","Computer"]

plt.bar(name,price,width=0.5, color="lightskyblue")

plt.show()


# In[ ]:




