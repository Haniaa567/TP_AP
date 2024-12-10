cities = []

while True:
    name=str(input("enter the name of the city: "))
    if(name.lower()=="stop"):
        break    
    population = len(name) * 1_000_000
    cities.append((name, population))

sorted_cities = sorted(cities, key=lambda x: x[1], reverse=True)
print("sorted cities: ")   
print(sorted_cities) 