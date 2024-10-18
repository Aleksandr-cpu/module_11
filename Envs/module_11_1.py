
import numpy as np

arr = np.arange(8, 20, 2, dtype=np.int64)
print(arr)

print(arr.size)

print(arr.reshape(2,3))

print(arr.sum())

added_array = arr + 6
print(added_array)

subtracted_array = arr - 3
print(subtracted_array)

multiplied_array = arr * 3
print(multiplied_array)

divided_array = arr // 2
print(divided_array)

