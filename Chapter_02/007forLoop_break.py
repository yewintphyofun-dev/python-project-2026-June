# for loop တွင်း break သုံးခြင်း
# break ရဲ့ အဓိပ္ပာယ်မှာ for loop တစ်ခုလုံးကို ရပ်လိုက်ခြင်း
for num in range(1,10):
    print(num)
    if num % 5 == 0:
        print("Successful!",num)
        break