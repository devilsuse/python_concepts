import numpy as np

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
print('before sort: ', arr)
np.sort(arr)
print('after sort: ', arr)
print('Printing func call: np.sort(arr): ', np.sort(arr))

ndArray = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])

print('ndim: ', ndArray.ndim)
print('size: ', ndArray.size)
print('shape: ', ndArray.shape)

data = np.array([1, 2])
ones = np.ones(2, dtype=int)
print('data + ones: ', data + ones)
print('data - ones: ', data - ones)
print('data * data: ', data * data)
print('data / data: ', data / data)

b = np.array([[1, 1], [2, 2]])
print('b.sum(axis=0): ', b.sum(axis=0))
print('b.sum(axis=1): ', b.sum(axis=1))

agg = np.array([[31,7,4,3,5],
                [4,7,14,2,15],
                [11,27,24,23,25],     
                [21,27,14,13,15]])
print('********* functional programming style - calls ****************')
print('np.min(agg) : ',np.min(agg))
print('np.max(agg) : ',np.max(agg))
print('np.sum(agg) : ',np.sum(agg))

print('********* Object-oriented programming style - calls ****************')
print('agg.min() : ',agg.min())
print('agg.max() : ',agg.max())
print('agg.sum() : ',agg.sum())
print('agg.min(axis=0) : ',agg.min(axis=0))
print('agg.max(axis=0) : ',agg.max(axis=0))
print('agg.sum(axis=0) : ',agg.sum(axis=0))


