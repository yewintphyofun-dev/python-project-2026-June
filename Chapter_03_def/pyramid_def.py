# pyramid တစ်ခုတည်ဆောက်သော def တစ်ခုတည်ဆောက်ခြင်း
# form နေရာတွင် ဘာမှ မပေးပါက default အနေဖြင့် * ဖြင့် ဖော်ပြလိမ့်မည်
def pyramid(num,form="*"):
    """
    ဒီfunction က pyramid တစ်ခုဆောက်ပေးတယ်
    Parameters:
    - num(int) : pyramid ရဲ့ လိုချင်တဲ့အမြင့်ကိုရေး
    - form(string) : pyramid တည်ဆောက်ချင်တဲ့ form ပုံစံ အက္ခရာ , default မှာ * ဖြစ်သည်
    Output -
    pyramid တစ်ခုတည်ဆောက်ပေးသည်
    """
    for i in range(num):
        print("   "*(num-1-i)+(form+"  ")*((2*i)+1))

pyramid(4,"#")
pyramid(6)

# အောက်တွင်ရေးထားသည်မှာ ယခုရေးထားသော pyramid function အကြောင်း ရှင်းပြထားသော doc string ဖြစ်သည်
print(pyramid.__doc__)