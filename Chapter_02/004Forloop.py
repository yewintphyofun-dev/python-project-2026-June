#For loop
for i in range(3):
    print("おはよう。")

#for loop testing
for num in range(4):
    print("Attempt",(num+1),(num+1)*".")


bigData = ["MgMg 29 163.2 WebDeveloper",
           "AyeAye 30 153.2 StaffOfficer",
           "MyaMya 42 152.5 Manager"]
for data in bigData:
    exampleList = data.split()[1]
    print(exampleList)