# NumPy (Numerical Python) is library used for handling arrays
# created by Travis Oliphant in 2005
# no real array data structure in Python as almost everything is object
# 50x faster than Python
# #1 library for data sciences and numerical methods when speed and memory consumption is crucial
# implemented in Python but most crucial operations are using C and C++

# list
"""
    list store references to objects
    each reference is 8 bytes
    not so efficient in memory consumption
 |______|  --------> |__34__|
 |______|  --------> |__56__|
 |______|  --------> |__12__|

    vs NumPy array store items in continuous block in memory
    items are right next to each other
"""

import numpy as np

print(np.__version__)
# create numpy array from list
python_list = [1, 2, 3, 4]
numpy_aray = np.array(python_list)
print(type(numpy_aray))
print(numpy_aray)

# we can store different type in Python list but not in NumPy
a = np.array([1, "Python", 3.5, True, 5])
# all items are converted to string: ['1' 'Python' '3.5' 'True' '5']
print(a)

# edit item based on index
a[0] = 10
print(a)

# insert item based on index
a = np.insert(a, 0, "Hello")
print(a)
