from ctypes import *
import numpy as np
from numpy.ctypeslib import ndpointer

class MyData(Structure):
    _fields_ = [
        ("a", c_int32, 8),
        ("b", c_int32, 8),
        ("c", c_int32, 8),
        ("d", c_int32, 8),
    ]

print('MyData size = ', sizeof(MyData))
print('MyData layout:', MyData.a, MyData.b, MyData.c, MyData.d, sep='\n')
print('MyData memoryview: ', memoryview(MyData()).format,  memoryview(MyData()).itemsize)

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

# pass python struct to cpp
f_print_struct = CDLL('./mylib.so').print_struct
my_data = MyData()
my_data.a, my_data.b, my_data.c, my_data.d = 1, 2, 3, 4
ptr_data = cast(pointer(my_data), POINTER(c_int8))
print('#### ptr_data address = ', hex(cast(ptr_data, c_void_p).value))
np_data = np.ctypeslib.as_array(ptr_data, shape=(sizeof(MyData),))
print('#### np_data pointer  = ', hex(np_data.__array_interface__['data'][0]), np_data)
f_print_struct.argtypes = [ndpointer(dtype=c_int8, shape=(np_data.size,))]
f_print_struct(np_data, np_data.size)

# all three pointers have same memory address
#### ptr_data address =  0x7ff238463a90
#### np_data pointer  =  0x7ff238463a90 [1 2 3 4]
#### print_struct: buf = 0x7ff238463a90, length = 4

print('done')