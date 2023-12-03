num = input("Please enter a number: ")
print(type(num))

num = int(num)
print(type(num))

if num % 2 == 0:
    print("The number is even")
elif num % 3 == 0 or num % 5 == 0:
    print("The number is divisible by 3 or 5")
else:
    print("This number is not special at all")
