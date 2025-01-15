def length(lst):
    n=0
    for item in lst:
        n=n+1
    return n

def mean(lst): 
    n=0
    if length(lst)==0:
        print("list vide")
        exit()
    for item in lst:
        try:
            n=float(item+n)
        except(ValueError):
            print("Input must be arithmetic.")
            exit()
    len=length(lst)
    mean=n/len
    if mean%1==0:
        mean=int(mean)
    if len==0:
        return None
    else:
        return mean
def range_of_list(lst):
    if length(lst)==0:
        print("list vide")
        exit()
    try:
        min=float(lst[0])
        max=float(lst[0])
    except ValueError:
        print("items must be arithmetic")
        exit()
    for item in lst:
        try:
            test=float(item)
        except ValueError:
            print("items must be arithmetic")
            exit()
        if test>max:
            max=test
        elif item<min:
            min=test
    range=(max-min)
    if range%1==0:
        range=int(range)
    return range
numbers = [1,2.4,-1,6]
print(length(numbers)) 
print(mean(numbers))
print(range_of_list(numbers))

        
