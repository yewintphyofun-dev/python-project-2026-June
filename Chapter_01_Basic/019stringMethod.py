#string method
fruit = "apple"
print(fruit.upper())

example = "    boolean data    "
# strip ဆိုတာ ရှေ့နဲ့နောက်က space အပိုတွေကို ဖြတ်ထုတ်ပစ်တာ
print(example.strip())
print(example.lstrip())
print(example.rstrip())
print(example.find("boolean"))

word = "hello, 1, 2,3"
#split ဆိုတာ ခွဲထုတ်တာ
print(word.split(","))
