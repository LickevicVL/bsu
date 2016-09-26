import numpy as np
import pandas as pd

"""1"""
def max_element(arr):
    if not arr.all() and not arr[:-1].all():
        m = arr.argmax()
        if m == 0 or arr[m - 1] != 0:
            if arr[m] == 0:
                return arr[m + 1]
            new_arr = np.hstack((arr[:m], arr[m + 1:]))
            return max_element(new_arr)
        else:
            return arr[m]
    elif arr == np.zeros(arr.shape):
        return 0
    elif arr.all():
        return None

print(max_element(np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])))
print(max_element(np.array([0, 0, -10, -3])))
print(max_element(np.array([10, 1, 0, -3, 0, 40, 0])))
print(max_element(np.array([0, 0, 0, 0])))
print('=================================================')

"""2"""
def nearest_value(X, v):
    mx = X[X >= v].min()
    mn = X[X < v].max()
    nearest = mx if abs(v - mx) < abs(v - mn) else mn
    return nearest

X = np.arange(0, 10).reshape((2, 5))
v = 3.6
print(nearest_value(X, v))
print('=================================================')

"""3"""

