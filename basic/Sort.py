def absolute(x):
    if x < 0:
        return -x
    else:
        return x

nums = [10, -4, 0, 4, 8, -9, 34, 100]

# sorted() always return a list
result = sorted(nums)
print(result)
descending = sorted(nums, reverse=True)
print(descending)

sort_absolute = sorted(nums, key=absolute)
print(sort_absolute)

# sort dicts
def key_value_tuple_sorter(x):
    return x[0]

people = {'Adam': 34, "Bill": 19, 'Kurt': 45, 'Hell': 90}
result = sorted(people.items(), key=dict_sorter)
print(result)
