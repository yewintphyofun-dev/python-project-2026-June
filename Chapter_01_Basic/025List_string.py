course = ["Myanmar","English","Math","Physics"]

# list ထဲကတန်ဖိုးတွေကို ဖြည်ချခြင်း
print(course)
course_str = " - ".join(course)
print(course_str)

# create new list
new_list = course_str.split(" - ")
print(new_list)

# list ထဲက တန်ဖိုးကိုလည်းပြောင်းလို့ရ
new_list[0] = "Art"
print(new_list)
