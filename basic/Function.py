# function: block of statements performing a specific task
# can define a default values for the params - if you call function without args, default value will be used
# body function cannot be empty
# if you want to leave the function empty, use keyword pass

# default value is Joe if not specified
def show_name(name="Joe"):
    # local variable
    age = 10
    print("The name of the person is " + name)
    print("The age of the person is {}".format(age))

show_name()
show_name("Kevin")

# empty function
def show_name_age(name, age):
    pass

print("Before calling")
show_name_age("Kevin", 10)
print("After calling")

# arg is a tuple, i.e. 1D array that can be accessed by index
def show_names(*names):
    for i in range(len(names)):
        print(names[i])

show_names("Kevin", "Adam", "Joe")


# arg is a dictionary - a map of key and value
def show_person(**params):
    print(params["fname"])
    print(params["lname"])
    print(params["age"])

show_person(fname="Kevin", lname="Clair", age=10)

# return single value
def add(num1, num2):
    return num1 + num2

print(add(10, 20))

# return multiple values
def withdraw(balance, amount):
    if amount < 0:
        return balance, False, "Cannot withdraw negative amount {}".format(amount)
    elif balance > amount:
        return balance - amount, True, ""
    else:
        return balance, False, "Cannot withdraw amount {} larger than balance {}".format(amount, balance)

new_balance, is_successful, error = withdraw(100, 200)
print(new_balance)
print(is_successful)
print(error)
result = withdraw(100, 50)
print(type(result)) # tuple
print(result[0]) # new balance
print(result[1]) # is successful
print(result[2]) # error


def recursive(text):
    recursive_visit(text, 0)
def recursive_visit(text, index):
    if index < len(text):
        print(text[index])
        recursive_visit(text, index+1)

recursive("diep")
