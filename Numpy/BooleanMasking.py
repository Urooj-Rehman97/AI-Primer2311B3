import numpy as np
arr = np.array([23,45,65,12,33,56,90])
a = arr>40
print(a)
print(arr>30)
combine_mask = (arr>40) & (arr<60)
print(arr[combine_mask])