mot=str(input("Please type in a string:" ))
v=['a','e','o']
for i in v:
    if mot.rfind(i)!=-1:
        print(i," found")
    else:
        print(i, "not found")  