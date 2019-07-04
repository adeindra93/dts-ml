import numpy as np
import matplotlib.pyplot as plt


new_array = np.empty([3,3], dtype=int)
row_number, col_number = new_array.shape

for row in range(row_number):
	for col in range(col_number):
		print(new_array[row][col])

print(new_array.shape)