nb=int(input("How many people need a ride? "))
tmp=int(input("How many people fit in one taxi? "))
if nb<0 or tmp<0:
    print("the values must be positive")
else:
    x=nb//tmp
    if nb%tmp!=0:
        x=x+1
    print("you need ", x ,"taxis")