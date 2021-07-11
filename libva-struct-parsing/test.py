import sys
from ctypes import *
import numpy as np
from numpy.ctypeslib import ndpointer

sys.path.append('build')
import pymylib as mylib

class MyData(Structure):
    _fields_ = [
        ("a", c_int32, 5),
        ("b", c_int32, 11),
        ("c", c_int32, 16),
        ("d", c_int8),
        ("e", c_int16),
        ("f", c_int16),
    ]

my_data = MyData()
my_data.a = 1
my_data.b = 2
my_data.c = 3
my_data.d = 4
my_data.e = 5
my_data.f = 6
ptr_data = cast(pointer(my_data), POINTER(c_int8))
print('#### ptr_data address = ', hex(cast(ptr_data, c_void_p).value))
np_data = np.ctypeslib.as_array(ptr_data, shape=(sizeof(MyData),))
print('#### np_data pointer  = ', hex(np_data.__array_interface__['data'][0]), np_data)
mylib.print_struct(np_data)

print('done')