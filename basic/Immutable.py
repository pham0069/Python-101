# immutable object: int, float, boolean, string, tuple
x = "5"
print(id(x)) # address of memory storing x

x = x+"1"
print(id(x)) # location has been changed

# mutable object: list, set, dict
l = [1, 2, 3, 4]
print(id(l))
l[0] = 10 # only change the content of the object
print(id(l)) # location is not changed
