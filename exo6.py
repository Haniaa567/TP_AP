price=float(input("Please type in a price:"))
if price>=0:
    print("Dinars:",int(price))
    print("Centimes",int((price - int(price)) * 100))
else:
    print("price must pe positive")