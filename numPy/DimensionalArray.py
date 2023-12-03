import numpy as np

n = np.array([1, 2, 3, 4, 5, 6])
print(n)
print(n.shape) # (6, )
print(n.ndim) # 1

n = np.array([[1, 2, 3], [4, 5, 6]])
print(n)
# 2 rows, 3 columns
print(n.shape) # (2, 3)
print(n.ndim) # 2
print(n[0]) # [1, 2, 3]
print(n[0][2]) # 3

for row in n: # [1,2, 3] and [4, 5, 6]
    for item in row:
        print(item)
#for index, row in enumerate(n):

# shape: number of items in each dimension
# reshape: change the shape of given array
nums = np.array([1, 2, 3, 4, 5, 6])
nums = nums.reshape(2, 3) # 2 rows, 3 columns
print(nums)

# use -1 for unknown dimension - Python/Numpy will find the number
nums = nums.reshape(6, -1)
print(nums)

# convert 2D into 1D
nums = np.array([[1, 2 , 3], [1, 2 , 3], [1, 2 , 3]])
# nums = nums.reshape(1, -1)[0]
nums = nums.reshape(-1)
print(nums)
