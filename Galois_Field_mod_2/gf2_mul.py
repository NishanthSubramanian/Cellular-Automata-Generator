import numpy as np
from Galois_Field_mod_2.functions import strip_zeros
from Galois_Field_mod_2.gf2_div import gf2_div
from Galois_Field_mod_2.gf2_mul_normal import gf2_mul_normal


def gf2_mul(a, b, p):
    mod_degree = len(p) -1
    fsize = len(a) + len(b) - 1
        
    fsize = 2**np.ceil(np.log2(fsize)).astype(int)  #use nearest power of two much faster

    fslice = slice(0, fsize)

    ta = np.fft.fft(a, fsize)
    tb = np.fft.fft(b, fsize)

    res = np.fft.ifft(ta*tb)[fslice].copy()

    k = np.mod(np.rint(np.real(res)), 2).astype('uint8')
    
    result = strip_zeros(k)
    if len(result) > mod_degree:
        q,result = gf2_div(result,p,p)
    return result