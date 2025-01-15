numbers = [1, 2, 3, 4, 5]
while True:
    i=int(input("Enter index (-1 to quit):"))
    if(i==-1):
        exit()
    elif(i>4 or i<0):
        print("index must be between 0 and 4")
        exit()
    v=int(input("Enter new value: "))

    numbers[i]=v
    print(numbers)    