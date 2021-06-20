from ctypes import *
import numpy as np
from numpy.ctypeslib import ndpointer

class MyData(Structure):
    _fields_ = [
        ("a", c_int32),
        ("b", c_int8),
        ("c", c_int16)
    ]
print('Mydata:', MyData.a, MyData.b, MyData.c, sep='\n')

# get array from cpp by using ctypes
f_get_array = CDLL('./mylib.so').get_array
f_get_array.restype = POINTER(c_int * 10)
print([i for i in f_get_array().contents])

# get array from cpp by using numpy.ctypeslib
f_get_array.restype = ndpointer(dtype=c_int, shape=(10,))
res = f_get_array()
print(type(res), res)

# python pass array to cpp
f_print_array = CDLL('./mylib.so').print_array
f_print_array.argtypes = [ndpointer(dtype=c_int, shape=(10,))]
indata = np.arange(10).astype(np.int32)
ptr = indata.__array_interface__['data'][0]
print(indata.__array_interface__['data'], hex(ptr)) # the ptr is exact same with the ptr used in c++ libarary
f_print_array(indata, indata.size)

print('done')