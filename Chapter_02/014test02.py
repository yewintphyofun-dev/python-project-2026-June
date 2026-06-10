# ထုတ်လို‌သော ပုံစံ
# *   
# *   *
# *   *   *   
# *   *   *   *

for i in range(4):
    for j in range(i+1):
        print("*",end="   ")
    print("")

# အပေါ်ကပုံစံနဲ့ ပြောင်းပြန်ပြန်ထုတ်ကြည့်မယ်
# ထုတ်လို‌သော ပုံစံ
# *   *   *   *
# *   *   *   
# *   *   
# *   
print("ဒုတိယ ပုံစံထုတ်ကြည့်ခြင်း")
for i in range(4):
    for j in range(i,4):
        print("*",end="   ")
    print("")