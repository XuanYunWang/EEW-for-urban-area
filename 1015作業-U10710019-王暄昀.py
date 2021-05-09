#!/usr/bin/env python
# coding: utf-8

# In[60]:


fp = open("bookinfo2.txt","r")
data=fp.readlines()
fp.close()

dict_book ={}
for i in data:
    i=i.rstrip("\n")
    temp=i.split(",")
    dict_book[temp[0]]=[temp[1],int(temp[2])]
    
User_input = "Y"

while (User_input=="Y" or User_input=="y"):
    print("----------------------------")
    print("1. 輸入資料 : ")
    print("2. 顯示資料 : ")
    print("3. 刪除資料 : ")
    print("4. 查詢資料 : ")
    print("5. 寫入檔案 : ")
    print("6. 計算總價 : ")
    print("7. 價錢分布 : ")
    print("8. 結束.")
    print("----------------------------")
    choice = input("Please select a choice:")
    print("----------------------------")
    print("Your choice is {}. ".format(choice))
    if choice=='1':
        print("--新增資料--")
        dict_book[input("請輸入書名 : ")]=[input("請輸入編號 : "),int(input("請輸入價錢 : "))]
    elif choice=='2':
        print("--顯示資料--")
        for i,j in dict_book.items():
            print(f"書名:{i},編號:{j[0]},價錢:{j[1]}")
    elif choice=='3':
        print("--刪除資料--")
        del dict_book[input("請輸入想要刪除的書名 : ")]
    elif choice=='4':
        print("----------------------------")
        print("1.利用書名查詢")
        print("2.利用編號查詢")
        print("----------------------------")
        choice = input("Please select a choice:")
        print("----------------------------")
        print("Your choice is {}. ".format(choice))
        if choice=='1':
            bookname=input("請輸入書名 : ")
            if bookname in dict_book.keys():
                print("----------------------------")
                print(f"書名:{bookname},編號:{dict_book[bookname][0]},價錢:{dict_book[bookname][1]}")
            else:
                print("----------------------------")
                print("很抱歉查無此書!請重新輸入")
        elif choice=='2':
            booknumber=input("請輸入編號 : ")
            for k,v in dict_book.items():
                if booknumber in v:
                    print("----------------------------")
                    print("書名:"+k+","+"編號:"+dict_book[k][0]+","+"價錢:"+str(dict_book[k][1]))
                    if booknumber in v:
                        break
            else:
                print("----------------------------")
                print("很抱歉查無此書!請重新輸入")
    elif choice=='5':
        print("--寫入檔案--")
        fp = open("bookinfo3.txt","w")
        for k,j in dict_book.items():
            fp.write(f"{k},{j[0]},{j[1]}""\n")
    elif choice=='6':
        print("--計算總價--")
        def function_sum1(dict_book):
            ans=0
            for i in dict_book.values():
                ans=int(ans)+int(i[1])
        
            return ans
        print("----------------------------")
        print(function_sum1(dict_book))

    elif choice=='7':
        print("--價錢分布--")
        print("----------------------------")
        get_ipython().run_line_magic('matplotlib', 'inline')
        import matplotlib.pyplot as plt

        y=[]
        for k in dict_book.values():
            y.append(k[1])  
        x=[]
        for i in dict_book.keys():
            x.append(i)
    
        plt.bar(x,y,width=0.5, color="lightskyblue")

        plt.show()
    elif choice=='8':
        User_input = "N"
        print("----------------------------")
        print("程式結束 !")


# In[ ]:




