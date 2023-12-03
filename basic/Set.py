# set is implemented with help of dictionary
# it uses array under the hood
# sets are unordered and unindexed - we dont know the position of the items
# set cannot store duplicate

# can use bracket like dictionary or set() function
my_set = {'Kevin', 34, 4.5, True}
my_set = set(('Kevin', 34, 4.5, True))

# the order of items changed compared to the tuple specified
print(my_set)

# cannot access set using index
# print(my_set[0])

# check existence in O(1)
if 34 in my_set:
    print("Included")
else:
    print("Not included")

# add new items
my_set.add("new")
my_set.update(['new', 55]) # 'new' is duplicate
print(my_set)

# iterate
for i in my_set:
    print(i)

# remove, discard
# remove raise error if the item is not present in the set
# discard does not raise error if the item is not present in the set
my_set.remove("Kevin")
my_set.discard("Daniel")
print(my_set)

# pop() removes the first item in the set
# non-deterministic function
my_set.pop()
print(my_set)

# union() joins 2 sets
set1 = {1, 10, "Kevin", 55}
set2 = {3, True, "Daniel", 55}
result = set1.union(set2)
print(result)
