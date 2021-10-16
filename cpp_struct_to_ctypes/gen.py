
def check_valid(line):
    if ';' not in line:
        return False
    else:
        return True

struct_name = 'H264PPS'
cpp_struct = []
output_list = []
output_list.append('from pstruct import *\n')
output_list.append('class %s(PStruct):' % struct_name)
output_list.append('    _fields_ = [')

with open('h264_pps.h', 'rt') as f:
    for line in f:
        if line.find('//') != -1:
            line = line[:line.find('//')]
        if len(line.strip()) == 0 or ('/*' in line and '*/' in line) or ('{' in line) or ('}' in line):
            continue
        cpp_struct.append(line.strip('\n').strip())

with open('h264_pps_new.h', 'wt') as f:
    f.writelines('\n'.join(cpp_struct))

for line in cpp_struct:
    if 'unsigned int' in line:
        s1 = line.split('unsigned int ')[1].split(';')[0]
        output_list.append('        ("%s", c_uint32),' % s1)
    elif 'uint32_t' in line:
        s1 = line.split('uint32_t ')[1].split(';')[0]
        output_list.append('        ("%s", c_uint32),' % s1)
    elif 'uint8_t' in line:
        s1 = line.split('uint8_t ')[1].split(';')[0]
        output_list.append('        ("%s", c_uint8),' % s1)
    elif 'int32_t' in line:
        s1 = line.split('int32_t ')[1].split(';')[0]
        output_list.append('        ("%s", c_int32),' % s1)
    elif 'size_t' in line:
        s1 = line.split('size_t ')[1].split(';')[0]
        output_list.append('        ("%s", c_uint64),' % s1)
    elif 'int' in line:
        s1 = line.split('int ')[1].split(';')[0]
        output_list.append('        ("%s", c_int32),' % s1)
    else:
        pass

output_list.append('    ]\n')

with open('dxva_def.py', 'wt') as f:
    f.writelines('\n'.join(output_list))

print('done')