import numpy as np
from Galois_Field_mod_2.functions import strip_zeros
import Galois_Field_mod_2

def gf2_div_normal(dividend, divisor):


    N = len(dividend) - 1
    D = len(divisor) - 1

    if dividend[N] == 0 or divisor[D] == 0:
        dividend, divisor = strip_zeros(dividend), strip_zeros(divisor)

    if not divisor.any():  # if every element is zero
        raise ZeroDivisionError("polynomial division")
    elif D > N:
        q = np.array([])
        return q,dividend

    else:
        u = dividend.astype("uint8")
        v = divisor.astype("uint8")

        m = len(u) - 1
        n = len(v) - 1
        scale = v[n].astype("uint8")
        q = np.zeros((max(m - n + 1, 1),), u.dtype)
        r = u.astype(u.dtype)

        for k in range(0, m - n + 1):
            d = scale and r[m - k].astype("uint8")
            q[-1 - k] = d
            r[m - k - n:m - k + 1] = np.logical_xor(r[m - k - n:m - k + 1], np.logical_and(d, v))

        r = strip_zeros(r)
        
    return q, r
