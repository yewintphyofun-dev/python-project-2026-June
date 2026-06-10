# definition များရေးသားခြင်း
# def တစ်ခု ရေးသားလိုက်တဲ့အခါ နောက်ပိုင်းလည်း ထို def ကို အကြိမ်ကြိမ် ပြန်ခေါ်သုံးလို့ရသွားသည်
def greet():
    print("မင်္ဂလာပါ")
    print("Nice to meet you.")
    print("初めまして！よろしくお願いします。")

# greet def ကို အောက်ပါအတိုင်းခေါ်သုံး၍ ရသည်
greet()

# .............................................................................

# area တွက်ချက်ခြင်း def တစ်ခုပြုလုပ်ခြင်း
# ဒီနေရာမှာ length နဲ့ width ကို parameters လို့ခေါ်တယ်
def rectangle_area(length,width):
    return length * width


area = rectangle_area(4,5)
# ဒီနေရာမှာ 4 သည် length , 5 သည် width ဖြစ်သည်။ 
# parameters များသည် ရှေ့နှင့်နောက် တည်နေရာအလိုက် အတိအကျယူ၍ နေရာအလွဲမခံပါ
print(area)