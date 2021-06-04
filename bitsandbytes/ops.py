import ctypes as ct
import bitsandbytes
import pathlib

funcs = ct.cdll.LoadLibrary(str(pathlib.Path().absolute()) + '/bitsandbytes/libClusterNet.so')

def testmul(A, scalar=1.0, out=None):
    if out is None: out = empty((A.shape[0],A.shape[1]))
    funcs.ffscalar_mul(ct.c_void_p(A.data.storage().data_ptr()), ct.c_void_p(out.data.storage().data_ptr()), ct.c_int32(A.numel()), ct.c_float(scalar))
    return out
