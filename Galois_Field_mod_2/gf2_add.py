import numpy as np
from Galois_Field_mod_2.functions import strip_zeros, check_type

def xor(a, b):
    return np.logical_xor(a, b, dtype='uint8').astype("uint8")

def gf2_add(a, b):
    a, b = check_type(a, b)
    a, b = strip_zeros(a), strip_zeros(b)
    N = len(a)
    D = len(b)
    if N == D:
        res = xor(a, b)
    elif N > D:
        res = np.concatenate((xor(a[:D], b), a[D:]))
    else:
        res = np.concatenate((xor(a, b[:N]), b[N:]))
    return strip_zeros(res)


