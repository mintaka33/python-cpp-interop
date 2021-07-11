import sys
from ctypes import *
import numpy as np
from numpy.ctypeslib import ndpointer

sys.path.append('build')
import pymylib as mylib

def print_memoryview(ctype):
    print(str(ctype), memoryview(ctype()).format, memoryview(ctype()).itemsize)
    pass

class VAPictureH264(Structure):
    _fields_ = [
        ("picture_id", c_uint32),
        ("frame_idx", c_uint32),
        ("flags", c_uint32),
        ("TopFieldOrderCnt", c_int32),
        ("BottomFieldOrderCnt", c_int32),
        ("va_reserved", c_uint32*4),
    ]

class VAPictureParameterBufferH264(Structure):
    _fields_ = [
        ("CurrPic", VAPictureH264),
        ("ReferenceFrames", VAPictureH264*16),
        ("picture_width_in_mbs_minus1", c_uint16),
        ("picture_height_in_mbs_minus1", c_uint16),
        ("bit_depth_luma_minus8", c_uint8),
        ("bit_depth_chroma_minus8", c_uint8),
        ("num_ref_frames", c_uint8),

        ("chroma_format_idc", c_uint32, 2),
        ("residual_colour_transform_flag", c_uint32, 1),
        ("gaps_in_frame_num_value_allowed_flag", c_uint32, 1),
        ("frame_mbs_only_flag", c_uint32, 1),
        ("mb_adaptive_frame_field_flag", c_uint32, 1),
        ("direct_8x8_inference_flag", c_uint32, 1),
        ("MinLumaBiPredSize8x8", c_uint32, 1),
        ("log2_max_frame_num_minus4", c_uint32, 4),
        ("pic_order_cnt_type", c_uint32, 2),
        ("log2_max_pic_order_cnt_lsb_minus4", c_uint32, 4),
        ("delta_pic_order_always_zero_flag", c_uint32, 1),

        ("num_slice_groups_minus1", c_uint8),
        ("slice_group_map_type", c_uint8),
        ("slice_group_change_rate_minus1", c_uint16),
        ("pic_init_qp_minus26", c_int8),
        ("pic_init_qs_minus26", c_int8),
        ("chroma_qp_index_offset", c_int8),
        ("second_chroma_qp_index_offset", c_int8),

        ("entropy_coding_mode_flag", c_uint32, 1),
        ("weighted_pred_flag", c_uint32, 1),
        ("weighted_bipred_idc", c_uint32, 2),
        ("transform_8x8_mode_flag", c_uint32, 1),
        ("field_pic_flag", c_uint32, 1),
        ("constrained_intra_pred_flag", c_uint32, 1),
        ("pic_order_present_flag", c_uint32, 1),
        ("deblocking_filter_control_present_flag", c_uint32, 1),
        ("redundant_pic_cnt_present_flag", c_uint32, 1),
        ("reference_pic_flag", c_uint32, 1),

        ("frame_num", c_uint16),
        ("va_reserved", c_uint32*8),
    ]

print_memoryview(VAPictureH264)
print_memoryview(VAPictureParameterBufferH264)
print('VAPictureParameterBufferH264 layout: ', 
    VAPictureParameterBufferH264.CurrPic, 
    VAPictureParameterBufferH264.ReferenceFrames, 
    VAPictureParameterBufferH264.frame_num,
    sep='\n')

# create ctypes structure from data pointer of numpy array
pic_size = memoryview(VAPictureParameterBufferH264()).itemsize
input_np = (np.ones((pic_size))*255).astype(np.uint8)
h264pic = VAPictureParameterBufferH264.from_address(input_np.ctypes.data)
print(h264pic.frame_num)

# create numpy array based on data pointer of ctypes structure
ptr = cast(pointer(h264pic), POINTER(c_int8))
np_data = np.ctypeslib.as_array(ptr, shape=(sizeof(h264pic),))
print(np_data.astype(np.uint8))

# input_np/h264pic/h264pic share same data pointer
np_data[-1] = 0
print(np_data.astype(np.uint8))
input_np[-2] = 0
print(np_data.astype(np.uint8))
h264pic.frame_num = 1
print(np_data.astype(np.uint8))

print('done')