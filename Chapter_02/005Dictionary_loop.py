# loop in dictionary
dict1 = {
    "name":"Mg Mg",
    "age":32,
    "position":"Developer"
}

# output keys
for x in dict1:
    print(x)

#output values
for x in dict1:
    print(dict1[x])

#output keys and value
for key,value in dict1.items():
    print(key,value)