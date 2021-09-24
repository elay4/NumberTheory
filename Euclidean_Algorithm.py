# finding the gcd of two natural numbers by the euclidean algorithm
# consensus: a,b two natural numbers where a < b
import sys

def divide_with_remainder(a, b):
    # b = a * q + r
    r = b % a
    q = int(b / a)
    return (q, r)

def euclidean_algo(a, b):
    if a == 0:
        return b
    (q, r) = divide_with_remainder(a, b)
    return euclidean_algo(r, a)

def extended_euclidean_algo(a, b):
    # initate
    # r_j =  s_j * a + t_j * b
    (r_prev, r) = (b, a)
    (s_prev, s) = (0, 1)
    (t_prev, t) = (1, 0)
    while r != 0:
        (q, res) = divide_with_remainder(r, r_prev)
        (r_prev, r) = (r, res)
        (s_prev, s) = (s, s_prev - q * s)
        (t_prev, t) = (t, t_prev - q * t)
    return (r_prev, s_prev, t_prev)

# returns (gcd, x, y) where x * a + y * b = gcd for a the min and b the max
def extended_gcd(num1, num2):
    a = min(num1, num2)
    b = max(num1, num2)
    return extended_euclidean_algo(a, b)

def gcd(num1, num2):
    a = min(num1, num2)
    b = max(num1, num2)
    return euclidean_algo(a, b)


(num1, num2) = tuple(map(int, sys.argv[1:])) 
print('The gcd of:', num1, ',', num2, 'is:', gcd(num1, num2))
print('The extended gcd of:', num1,',', num2, 'is:', extended_gcd(num1, num2))