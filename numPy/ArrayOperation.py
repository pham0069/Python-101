import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = np.vstack((a, b))
print(result)

result = np.hstack((a, b))
print(result)

odd = a % 2 != 0 # True, False, True
result = a[odd]
print(result)
