try:
    n=int(input("enter a postive number: "))
except(ValueError):
    print("number must be integer")
    exit()
if n<0:
    print("number must be positve")
    exit()
for i in range(-n,n):
        print(i)