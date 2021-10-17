
def check_valid(line):
    if ';' not in line:
        return False
    else:
        return True

def parse_array_name(name):
    dim = []
    pos = name.find('[')
    if '[' in name:
        s0, s1 = name[:pos], name[pos:]
        dim = s1.replace('[', '').split(']')
        dim = [int(s, 10) for s in dim if s != '']
        return s0, dim
    else:
        return name, dim

def get_type_name(line):
    var_type, var_name, dim =  None, None, []
    if 'unsigned int' in line:
        var_type = 'c_uint32'
        var_name = line.split('unsigned int ')[1].split(';')[0]
    elif 'uint32_t' in line:
        var_type = 'c_uint32'
        var_name = line.split('uint32_t ')[1].split(';')[0]
    elif 'uint8_t' in line:
        var_type = 'c_uint8'
        var_name = line.split('uint8_t ')[1].split(';')[0]
    elif 'int32_t' in line:
        var_type = 'c_int32'
        var_name = line.split('int32_t ')[1].split(';')[0]
    elif 'size_t' in line:
        var_type = 'c_uint64'
        var_name = line.split('size_t ')[1].split(';')[0]
    elif 'int' in line:
        var_type = 'c_int32'
        var_name = line.split('int ')[1].split(';')[0]
    else:
        return None, None, []
    var_name, dim = parse_array_name(var_name)
    return var_type, var_name, dim

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
    vtype, vname, dim = get_type_name(line)
    if vtype != None and vname != None:
        if len(dim) == 0:
            output_list.append('        ("%s", %s),' % (vname, vtype))
        else:
            type_str = vtype
            for d in dim:
                type_str = '(%s)*%d' % (type_str, d)
            output_list.append('        ("%s", %s),' % (vname, type_str))

output_list.append('    ]\n')

with open('dxva_def.py', 'wt') as f:
    f.writelines('\n'.join(output_list))

print('done')