import numpy as np
import pandas as pd

"""1"""
def max_element(arr):
    if not arr.all() and not arr[:-1].all():
        m = arr.argmax()
        if m == 0 or arr[m - 1] != 0:
            if arr[m] == 0:
                if 0 not in arr[m + 1:]:
                    return arr[m + 1]
                elif arr[m + 1] == 0:
                    return 0
                else:
                    new_arr = arr[m + 1:]
                    return max_element(new_arr)
            new_arr = np.hstack((arr[:m], arr[m + 1:]))
            return max_element(new_arr)
        else:
            return arr[m]
    elif arr == np.zeros(arr.shape):
        return 0
    elif arr.all():
        return None

print(max_element(np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])))
print(max_element(np.array([-15, 0, -10, 0, -3])))
print(max_element(np.array([10, 1, 0, -3, 0, 1, 0])))
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
def scale(X):
    TX = X.transpose()
    def sc(arr):
        sample_mean = arr.sum() / len(arr)
        n = len(arr) - 1
        if n != 0:
            standard_deviation = (sum((arr - sample_mean)**2) / n)**0.5
            return (arr - sample_mean) / standard_deviation
        else:
            return 0
    return np.array(list(map(sc, list(TX)))).transpose()


X = np.random.randint(10, size=(3, 3))
print(X)
print(scale(X))
print('=================================================')

"""4"""
def get_stats(X):
    determinant = np.linalg.det(X)
    trace = np.trace(X)
    mn, mx = X.min(), X.max()
    norm = np.linalg.norm(X)
    eigenvalues = np.linalg.eigvals(X)
    inv = np.linalg.inv(X)
    return determinant, trace, (mn, mx), norm, eigenvalues, inv

print(get_stats(X))
print('=================================================')

"""5"""
l = list()
for i in range(100):
    M = np.random.normal(size=(10, 10))
    N = np.random.normal(size=(10, 10))
    MN = M.dot(N)
    l.append(MN.max())
al = np.array(l)
average = sum(al) / len(al)
quantile = np.percentile(al, 95)
print(average, quantile)