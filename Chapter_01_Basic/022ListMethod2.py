# List Method 02
course1 = ["Myanmar","English","Math"]
course2 = ["Japanese","Science"]

#   append နဲ့ ပေါင်းရင် list လိုက်ကြီးပဲ အထဲကိုဝင်သွားတယ်
#   course1.append(course2)
#   print(course1)

#   insert ဆိုတာက append နဲ့ အတူတူပဲ။ ကွာခြားချက်က ထည့်ချင်တဲ့နေရာကိုရွေးပေးလို့ရတယ်
#   course1.insert(1,course2)
#   print(course1)

#   extend ဆိုရင် အထဲက list ကို ဖြေပြီး ပေါင်းပေးမယ်
course1.extend(course2)
print(course1)

#   remove ဆိုရင် ဖြုတ်
course1.remove("Math")
print(course1)

#   pop ဆိုရင်လည်း ဖြုတ်တာပဲ။ ဒါပေမဲ့ index နံပါတ်နဲ့ရွေးဖြုတ်တာ
course1.pop(1)
print(course1)

# pop ကို variable တစ်ခုနဲ့ ယူလို့လည်းရ
popped_subject = course1.pop(0)
print(popped_subject)