import numpy as np

a = np.array([1,2,3])
print(a)

zeros = np.zeros(3)
print (zeros)

ones = np.ones(3)
print (ones)

empty = np.empty(33)
print (empty)

arange = np.arange(5)
print (arange)

firstLastStep = np.arange(2,17,2)
print ('firstLastStep: ', firstLastStep)

linspace = np.linspace(0,10,num=5)
print('linspace: ', linspace)
print('type(linspace): ', type(linspace))

np_int64 = np.ones(12, dtype=np.int64)
print('np_int64: ', np_int64)

