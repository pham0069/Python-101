# usually it's called array - but in Python it's called list
# The implementation uses a contiguous array of references to other objects,
# and keeps a pointer to this array and the array’s length in a list head structure."

# if you want to use array - then use NumPy arrays
# this is 50 times faster than traditional Python list
a = [1, 2, 3, 4]
b = list((1, 2, 3, 4))
mixed = ["Kevin", 10, 4.5]

print(a)
print(b)
# type is list
print(type(a))
# use built-in function len to get size of list
print(len(a))
# access item based on index
print(a[0]) # first item
print(a[-1]) # last item
print(a[0:2]) # sublist with given index range

print(mixed)

# edit list item
mixed[0] = "Daniel"
print(mixed)

# delete item based on index
del mixed[0]
print(mixed)

# append new item
mixed.append("hell")
print(mixed)

# can contain duplicate value
mixed.append("hell")
print(mixed)

# concatenate
list1 = [1, "list1", 3.5]
list2 = [True, "list2", False]
list1.extend(list2)
print(list1)

# copy
list3 = list2.copy()
list3.append("hey")
list3[2] = 0
print(list2) # change in list3 not affecting list2
print(list3)

# remove item based on value
mixed.remove('hell')
print(mixed)

# remove last item O(1)
result = mixed.pop() # return last item
print(result)
print(mixed)

# reverse the list order
mixed.reverse()
print(mixed)

# sort
rand = [10, 2, 5, 8, 1, 9, 4, 6, 3, 7]
rand.sort()
print(rand)

# comprehension
even = [i for i in rand if i % 2 == 0]
print(even)

# insert - take O(n) as it needs shifting all the items after index to the right
rand.insert(2, 11)
print(rand)
