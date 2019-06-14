import numpy as np
from Galois_Field_mod_2.functions import strip_zeros, Reverse
from Galois_Field_mod_2.gf2_div import gf2_div
from Galois_Field_mod_2.gf2_mul_normal import gf2_mul_normal
from Galois_Field_mod_2.gf2_div_normal import gf2_div_normal



def isGreater(a,b):
    a_rev = Reverse(a)
    b_rev = Reverse(b)
    if len(a) > len(b):
        return True
    elif len(a) < len(b) :
        return False
    else : 
        for i in range(len(a_rev)):
            for j in range(len(b_rev)):
                if a_rev[i]==b_rev[j]:
                    i+=1
                    j+=1
                elif a_rev[i] > b_rev[j]:
                    return True
                else:
                    return False
    return

def gf2_mul(a, b, p):
    mod_degree = len(p) -1
    fsize = len(a) + len(b) - 1
        
    fsize = 2**np.ceil(np.log2(fsize)).astype(int)  #use nearest power of two much faster

    fslice = slice(0, fsize)

    ta = np.fft.fft(a, fsize)
    tb = np.fft.fft(b, fsize)

    res = np.fft.ifft(ta*tb)[fslice].copy()

    k = np.mod(np.rint(np.real(res)), 2).astype('uint8')

    # temp = Reverse(a)
    
    # print("---")
    # for i in temp:
    #     print(i,end="")
    # print("end---")
    result = strip_zeros(k)

    if isGreater(result,p):
        q,result = gf2_div_normal(result,p)
    return result