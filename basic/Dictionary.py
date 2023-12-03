# key- value map
# key is mapped to an integer using a hash function
# that defines the slot/index on the 1D array that stores the value

my_dict = {"name": "Kevin", "gender": "male", "age": 35, 13: False, True: "single"}

print("name" in my_dict)
# access value using key
print(my_dict["name"])
print(my_dict[True])


# for non-existent key, will throw KeyError
# print(my_dict["hell"])

# access keys
for key in my_dict.keys():
    print(key)

# access values
for value in my_dict.values():
    print(value)

# access key-value pairs
for key, value in my_dict.items():
    print(key, str(value))

# use zip to access key-value pairs
for key, value in zip(my_dict.keys(), my_dict.values()):
    print(key, str(value))

# edit value of existing key
my_dict["name"] = "Adam"

# add key-value
my_dict["country"] = "US"
print(my_dict)

# delete key
del my_dict["name"]
print(my_dict)

# length
print(len(my_dict))

# create dictionary with dict() built-in function
# cannot use boolean/number as key 13=False, True="single"
kevin = dict(name="Kevin", gender="male", age=35)
print(kevin)

# nested dictionary
name = {"name": {"first_name":"Kevin", "last_name":"Claire"}}
print(name["name"]["first_name"])
print(name["name"]["last_name"])
