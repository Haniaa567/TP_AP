from math import sqrt
while True:
    n=int(input("number? :"))
    if n==0:
        break
    if n>0:
        print("racine: ",sqrt(n))
    else :
        print("invalid")
        