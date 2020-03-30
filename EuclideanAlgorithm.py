s1 = 4
s2 = 5
c = 21

# Extended Euclidean Algorithm: ax + by = gcd(a, b)

def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)

print(gcd(30,20))


def gcdExtended(a, b, x, y):
    # Base Case
    if a == 0:
        x = 0
        y = 1
        return b

    x1 = 1
    y1 = 1  # To store results of recursive call
    gcd = gcdExtended(b % a, a, x1, y1)

    # Update x and y using results of recursive
    # call
    x = y1 - (b / a) * x1
    y = x1

    return gcd


x = 1
y = 1
a = 35
b = 15
g = gcdExtended(a, b, x, y)
print("gcd(", a, ",", b, ") = ", g)


def e(a, b):
    r = b
    x = a    # becomes gcd(a, b)
    s = 0
    y = 1    # the coefficient of a
    t = 1
    z = 0    # the coefficient of b
    while r:
        q = x / r
        x, r = r, x % r
        y, s = s, y - q * s
        z, t = t, z - q * t
    return y % (b / x), z % (-a / x) # m

print(e(4,5))