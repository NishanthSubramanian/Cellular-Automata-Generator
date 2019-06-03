import numpy as np
from Galois_Field_mod_2 import gf2_add, gf2_mul, gf2_div, strip_zeros,gf2_mul_normal,gf2_div_normal
from Galois_Field_mod_2 import functions
from Galois_Field_mod_2.functions import Reverse, trans

# Defining Trace as Tr(a) = (a + a^2 + a^4 + ..... + a^(2^(n-1)))mod p
def Trace(a,n):
    sum = np.array([],dtype="uint8")
    for i in range(n):
        term=a
        for j in range(i):
            term = gf2_mul(term,term,p)    
        sum = gf2_add(sum,term)
    return sum

# For all polynomials with degree less than n, find those polynomials with trace = 1
def findUnitTrace(n):
    total_num_of_polynomials = 2**n
    for num in range(1,total_num_of_polynomials):
        a = np.array(Reverse(trans(num)))
        if np.array_equal(Trace(temp_array,n),[1]):
            print(Trace(temp_array,n))
            break
    return a

# beta(x) = g*thetha(x)^2 + (g + g^2)thetha(x)^4 + ..... + (g + g^2 + ..... + g^(2^(n-1)))*thetha(x)^(2^(n-1))
def beta(g,thetha,n):
    final_sum=np.array([0],dtype="uint8")
    for i in range(1,n):
        inner_sum = np.array([],dtype="uint8")
        for j in range(i):
            inner_term=g
            for k in range(j):
                inner_term = gf2_mul(inner_term,inner_term,p)
            inner_sum = gf2_add(inner_sum,inner_term)
        thetha_term = thetha
        for l in range(i):
            thetha_term = gf2_mul(thetha_term,thetha_term,p)
        inner_full_sum = gf2_mul(inner_sum,thetha_term,p)
        final_sum = gf2_add(final_sum,inner_full_sum)
    return final_sum

# GCD of two polynomials
def gcd(p,q):
    ca = []
    a = p
    b = q
    while not np.array_equal(b,[1]):
        q_temp,r_temp = gf2_div_normal(a,b)
        a = b
        b = r_temp
        ca.append(q_temp[0])
    ca.append(a[0])
    return ca

def printPolynomial(a):
    degree = 0
    for i in a:
        if degree == len(a)-1:
            print("x^" + str(degree),end="")
        elif i != 0:
            print("x^" + str(degree) + " + ",end="")
        degree+=1
    print()      

# p is an irreducible polynomial
p =np.array([1, 0, 0, 1, 0, 1], dtype="uint8")              # Here, p is x^5 + x^3 + 1

# p_prime (or p') is the first derivative of polynomial p
p_prime = np.array([0, 0, 1, 0, 1], dtype="uint8")

temp = np.array([0,1,1],dtype="uint8")

# f = (x^2 + x)p'(x)
f = gf2_mul(p_prime,temp,p)
print("f(x) is " ,end="")                                
printPolynomial(f)

unit = np.array([1],dtype="uint8")
f_inverse, remainder = gf2_div(unit,f,p)

# g = (1/f)^2
g = gf2_mul(f_inverse,f_inverse,p)             
print("g(x) is ",end="")
printPolynomial(g)

# n = degree(p)
n = len(p) - 1
print("n is " + str(n))


temp_array = np.array([0,0,0,1], dtype="uint8")

# If n is even, find a thetha(x) with trace one, and compute beta(x)
if n%2 ==0:     
    thetha = findUnitTrace(n)
    # print(thetha)
    beta = beta(g,thetha,n)
# If n is odd, use thetha(x) = 1, and compute beta(x)
else:
    thetha = np.array([1], dtype="uint8")
    beta = beta(g,thetha,n)

print("Beta(x) is ",end="")
printPolynomial(beta)

q = gf2_mul(beta,f,p)
print("q(x) is ",end="")
printPolynomial(q)

# Final Cellular automaton is the gcd of p and q
ca = gcd(p,q)
print("Final CA is " + str(ca))
