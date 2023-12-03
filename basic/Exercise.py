num = "1"
num = int(num)

if num < 0:
    print("The number is smaller than 0")
elif num <= 10:
    print("The number is within the range [0, 10]")
else:
    print("The number is larger than 10")


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for number in array:
    sum+= number
else:
    print("Average: ", sum/len(array))


def is_prime(x):
    if x == 0:
        return False
    elif x == 1:
        return False
    elif x == 2:
        return True

    for i in range(2, x-1):
        if x % i == 0:
            return False

    return True

numbers = [1, 5, 43, 55, 76, 100, 123, 11, 2, -5, 87, 99]
prime = [n for n in numbers if is_prime(n)]
print(prime)

square = [n**2 for n in range(5, 11)]
print(square)

names = ['Adam', 'Daniel', 'Ana']
ages = [34, 12, 54]
my_dict = {}
#for i in range(len(names)):
#    my_dict[names[i]] = ages[i]

for key, value in zip(names, ages):
    my_dict[key] = value
print(my_dict)


class Car:
    color = "black"

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def get_brand(self):
        return self.brand

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

c = Car('Toyota', 2000)
print(c.get_color())
print(c.get_brand())
print(c.get_year())
