#use input function to take user's input
mark = input("Enter your mark : ")

# change data type
mark = int(mark)

# if statement
if mark < 0 or mark > 100:
    print("Wrong Input Mark!")
elif mark >= 60:
    print("pass exam.")
else:
    print("fail exam.")

print("done")