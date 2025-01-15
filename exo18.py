List= [1, 2, 3, 4, 5]
print("Menu:\n\n1.Append\n2.Insert\n3.Pop\n4.Remove\n5.Quit\n6.Search\n")
opt=int(input("Choose an option: "))

if (opt==1):
    v=int(input("enter value to append: "))
    List.append(v)
    print(List)
elif(opt==2):
    v=int(input("enter an element to instert: "))
    List.insert(v)
    print(List)
elif(opt==3):
    element=int(List.pop())
    print("poped element: ",element)
    print(List)
elif(opt==4):
    v=int(input("enter an element to remove: "))
    if v in List:
        List.remove(v)
        print(List)
    else:
        print("valeur n'existe pas")
elif(opt==5):
    print(List)
    exit()
elif(opt==6):
    v=int(input("enter an element to search: "))
    i=0

    try:
        i=List.index(v)    
    except ValueError:
        print("valeur n'existe pas")
        print(List)
        exit()
    print("value is in position ",i,"\n")

    
else:
    print("erreur valeur invalide")