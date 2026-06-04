# list method
marks = [54,55,52,64,53]
print(marks)
print(len(marks))
print(max(marks))
print(min(marks))
print(sum(marks))
print(sorted(marks))

subject = ["Myanamr","English","Math","Japanese","Science"]
print(subject[0][0])

#   list ထဲ တန်ဖိုးအသစ်ထည့်ခြင်း
subject.append("History")
print(subject)

#   ကိုယ်ထည့်ချင်တဲ့နေရာမှာ တန်ဖိုးထည့်ခြင်း
subject.insert(1,"Art")
print(subject)