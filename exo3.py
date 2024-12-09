total=int(input("Total amount: "))
nb=int(input("Number of items: "))
day=input("Day of the week: ").lower()
error=False
if day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    dis = 0.10 
elif day in ["saturday", "sunday"]:
    dis = 0.20
else:
    print("Invalid day")
    error=True
if(nb<0):
    error=True
elif nb>5:
    dis=dis+0.05
if error==False:   
    print("Total price after discount: ",total-total*dis)
