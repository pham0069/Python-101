import collections

linked_list = collections.deque([])

# insert to the end
linked_list.append(10)
linked_list.append("Adam")
linked_list.append(False)

# insert to the start
linked_list.appendleft("new")

# access by index - but it's not random access like array
# needs to traverse the list until reaching the index - O(n)
print(linked_list[2])
print(linked_list)
