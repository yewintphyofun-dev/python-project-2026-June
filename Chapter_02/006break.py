successful = True
for i in range(3):
    print("Attempt")
    if successful:
        print("successful")
        break

fruits = ["apple","orange","mango"]
for fruit in fruits:
    print(fruit)
    if fruit == "orange":
        print("successful")
        break