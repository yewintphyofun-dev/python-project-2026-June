# အရင်ဆုံး random ဆိုတဲ့ library တစ်ခုကို ခေါ်ထည့်လိုက်တယ်
import random

# အောက်ပါ loop တွင် True ကျမလား False ကျမလားဆိုသည်ကို random သတ်မှတ်သည်
# False ကျပါက You can pass ဟု print ထုတ်ပြီး နောက်တစ်ကြိမ် while loop ပတ်သည်
# True ကျပါက name ၏ value ဖြစ်သော John Done ကို print ထုတ်ပြပြီး loop ထဲက ထွက်သွားသည်
while True:
    pessenger = {
    "name" : "John Done",
    "random_choice" : random.choice([True,False])
    }

    if pessenger["random_choice"]:
        print(pessenger["name"])
        break
    else:
        print("You can pass.")