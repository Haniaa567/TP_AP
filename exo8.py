num=int(input("number:"))
if(num%3==0 and num%5==0):
    print("FizzBuzz")
elif(num%3==0):
    print("Buzz")
elif(num%5==0):
    print("Fizz")