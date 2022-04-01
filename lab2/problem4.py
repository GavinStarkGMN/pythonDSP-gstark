import numpy as np
import time

def numpy_minmax(arr):
    return arr.min(), arr.max()

def my_minmax(arr):
    min, max = arr[0][0], arr[0][0]
    for row in arr:
        for n in row:
            if n < min:
                min = n
            if n > max:
                max = n
    return min, max


rnd = np.random.rand(1000,1000)

start_time = time.time()
mina, maxa = numpy_minmax(rnd)
numpy_time = time.time()
minb, maxb = my_minmax(rnd)
my_time = time.time()

if mina == minb and maxa == maxb:
    print('My function works')
else:
    print('My function is broken')

print('Numpy took {} seconds to complete'.format(numpy_time - start_time))
print('My function took {} seconds to complete'.format(my_time - numpy_time))
print('Total execution was {} seconds'.format(my_time - start_time))
