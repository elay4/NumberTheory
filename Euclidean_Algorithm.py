# finding the gcd of two natural numbers by the euclidean algorithm
# consensus: a,b two natural numbers where a < b

def divide_with_reminder(a, b):
    # b = a * q + r
    r = b % a
    q = int(b / a)
    return (q, r)

def euclidean_algo(a, b):
    if a == 0:
        return b
    (q, r) = divide_with_reminder(a, b)
    return euclidean_algo(r, a)

def extended_euclidean_algo(a, b):
    # initate
    # r_j =  s_j * a + t_j * b
    (r_prev, r) = (b, a)
    (s_prev, s) = (0, 1)
    (t_prev, t) = (1, 0)
    while r != 0:
        (q, res) = divide_with_reminder(r, r_prev)
        (r_prev, r) = (r, res)
        (s_prev, s) = (s, s_prev - q * s)
        (t_prev, t) = (t, t_prev - q * t)
    return (r_prev, s_prev, t_prev)

def extended_gcd(num1, num2):
    a = min(num1, num2)
    b = max(num1, num2)
    return extended_euclidean_algo(a, b)

def gcd(num1, num2):
    a = min(num1, num2)
    b = max(num1, num2)
    return euclidean_algo(a, b)

num1, num2 = 873, 5418

print(gcd(num1, num2))
(d, x, y)=extended_gcd(num1, num2)
print(x * num1 + y * num2, "and the gcd:", d)