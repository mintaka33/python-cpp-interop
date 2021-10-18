from ctypes import *

class sHeader(Structure):
    _fields_ = [
        ("CC",  c_uint32, 4),
        ("AFC", c_uint32, 2),
        ("TSC", c_uint32, 2),
        ("PID", c_uint32, 13),
        ("TP",  c_uint32, 1),
        ("PSI", c_uint32, 1),
        ("TEI", c_uint32, 1),
        ("SyncByte", c_uint32, 8)
    ] # note: added 8 here

class Header(Union):
    _fields_ = [
        ("sData", sHeader),
        ("ulData", c_uint32)
    ]

head = Header()
head.ulData = 0xffffffff
print('head.ulData = 0x%x'%head.ulData)

for i in sHeader._fields_:
    exp = 'head.sData.%s'%i[0]
    print(exp, ' = 0x%x'%eval(exp))

print('done')