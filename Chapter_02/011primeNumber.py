# 2 မှစ၍ user ထည့်ပေးသော ကိန်းအတွင်း ရှိသမျှ သုဒ္ဓကိန်းများထုတ်ပေးခြင်း
while True:
    num = int(input("Enter number to find prime numbers under this number:"))
    if num < 2:
        print("Please input another number!!")
    elif num == 2:
        print(num)
    else:
        for allint in range(2,num+1):
            for i in range(2,allint):
                if allint % i == 0:
                    break
            else:
                print(allint,end=" ")       
    break
