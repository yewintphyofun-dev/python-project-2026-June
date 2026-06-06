# for loop တွင်း continue သုံးခြင်း
# continue အဓိပ္ပာယ်မှာ လက်ရှိလုပ်နေသော အခေါက်ကိုသာ ရပ်ပစ်ခြင်း

fruits = ["apple","orange","banana"]
for fruit in fruits:
    if fruit == "orange":
        continue            # orange အလှည့်တွင် အောက်က print function မrun ဘဲ ကျော်လိုက်ခြင်း
    print(fruit)