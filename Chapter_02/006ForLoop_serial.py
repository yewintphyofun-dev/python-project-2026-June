# serial data များတွင် loop ပတ်ခြင်း

# 1. string data for loop ပတ်ခြင်း
for char in "apple":
    print(char)

# 2. list data for loop ပတ်ခြင်း
for fruit in ["apple","banana","orange"]:
    print(fruit)

job_data = [
    "MgMg 20 developer",
    "AyeAye 23 casher",
    "MyaMya 30 Director"
]

for i in job_data:
    age = i.split()[1]
    print(age)

# 3. tuple data for loop ပတ်ခြင်း
for fruit in ("apple","banana","orange"):
    print(fruit)

# 4. set data for loop ပတ်ခြင်း
# set data ရဲ့ ထူးခြားချက်မှာ {}အတွင်း data များကို အစီအစဉ်တကျမဟုတ်ဘဲ ထုတ်ချင်သလို ထုတ်ပေးခြင်းဖြစ်
for fruit in {"apple","banana","orange"}:
    print(fruit)

# 5. dictionary data for loop ပတ်ခြင်း
car = {
    "car":"Ford",
    "model":"Mustang",
    "year" : 2024
}

for i in car:
    print(i)
    
for i in car:
    print(car[i])

for key,value in car.items():
    print(key,value)