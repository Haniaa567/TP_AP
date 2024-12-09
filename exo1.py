name=input("Please enter your name: ")
if name!="VIP":
    nb=int(input("How many tickets would you like to buy? "))
    if nb<0:
        print("number must be positive")
    else:
        print("The total cost is ",nb*15.5)
        print("Enjoy your tickets!")
else:
    print("Enjoy the show for free!")