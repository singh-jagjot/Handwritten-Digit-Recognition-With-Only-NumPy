import numpy as np
a = np.arange(9).reshape((3,3))
b = np.max(a, axis=1).reshape((a.shape[0], 1))
print(a)
# print(b)
# print(a - b)
c = np.sum(a, axis=1).reshape((-1, 1))
print(c)
print(a/c)