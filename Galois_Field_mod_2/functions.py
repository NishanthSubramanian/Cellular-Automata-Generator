import numpy as np

# Reverse a list
def Reverse(lst): 
    return [ele for ele in reversed(lst)] 

# Convert a binary number to a list
def trans(x):
    if x == 0: return [0]
    bit = []
    while x:
        bit.append(x % 2)
        x >>= 1
    return bit[::-1]

# Strip un-necessary leading (rightmost) zeroes from a polynomial
def strip_zeros(a):
    return np.trim_zeros(a, trim='b')

# Type check and force cast to uint8 ndarray
def check_type(a, b):

    if isinstance(a, np.ndarray):
        a = np.array(a, dtype="uint8")

    if isinstance(b, np.ndarray):
        b = np.array(b, dtype="uint8")

    if a.dtype is not "uint8":
        a = a.astype("uint8")

    if b.dtype is not "uint8":
        b = b.astype("uint8")

    return a, b

# Zero-pad input array a a to length dim, zeroes are appended at the right
def padding(a, dim):
    return np.pad(a, (0, dim-len(a)), 'constant', constant_values=(0))

# Given two arrays a and b returns the two arrays with the shorter zero-padded to have the same dimension of the longer. The arrays are padded with zeroes appended to the right.
def to_same_dim(a, b):
    if len(a) > len(b):
       return a, padding(b, len(a))

    elif len(a) < len(b):
        return padding(a, len(b)), b

    else:
        return a, b

# Returns dim coefficients for -1 degree polynomial
def zeros(dim):
    return np.zeros(dim, dtype='uint8')

# Returns dim coefficients for a zero degree polynomial
def zerodegree_pol(dim):
    out = zeros(dim)
    out[0] = 1

    return out
