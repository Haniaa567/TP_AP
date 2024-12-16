i=1
j=1
while True:
    n=int(input("number positive? :"))
    if n>0:
        break
while i<=n:
    j=1
    while j<=n:
        print(i,"*",j)
        j=j+1
    i=i+1
