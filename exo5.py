print("Runner 1")
name1 = input("Enter the name of the first runner: ")
time1 = float(input("Time (in seconds): "))

print("Runner 2")
name2 = input("Enter the name of the second runner: ")
time2 = float(input("Time (in seconds): "))

if time1 < 0 or time2 < 0:
    print("Times must be positive")


if time1 < time2:
    print(name1," is the faster runner")
elif time2 < time1:
    print(name2," is the faster runner")
else:
    print(name1," and ",name2," have the same time.")