# dictionary တည်ဆောက်ခြင်း
employee = {
    "name":"Phyo",
    "age":24,
    "position":"system developer",
    "experience":0.4,
    "language":["myanmar","english","japanese"]
}

print(employee)
print(type(employee))

# တန်ဖိုးအသစ်ထည့်ခြင်း
employee["hair_color"] = "black"
print(employee)

# တန်ဖိုးထုတ်ခြင်း
print(employee["name"])
print(employee.get("name"))

# keys များကိုသာ သီးသန့်ထုတ်ခြင်း
print(employee.keys())

employee_name = employee["name"]

employee.pop("age")

# popitem ဆိုတာ နောက်ဆုံးက value ကိုဖျက်
employee.popitem()

# copy အသစ်ကူး
employee_new = employee.copy()