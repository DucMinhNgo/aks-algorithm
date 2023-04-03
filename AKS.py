import math
from sage.all import *
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
from sage.rings.integer_ring import ZZ

# Kiển tra 1 số có viết được dưới dạng a^b hay không
# flat = True (composite)


def testing_for_perfect_power(n):
    b = 2
    a = 0
    log2_n = math.log2(n)
    flat = False
    while (b <= log2_n):
        y = (log2_n / b)
        a = int(pow(2, y))

        if (pow(a, b) == n):
            flat = True
            break

        b += 1
    return (flat, a, b)


def find_an_appropriate_r(n):
    r = 2
    log2_n = math.log2(n)
    output = 0
    while (r <= pow(log2_n, 5) + 1):
        k = 1
        flat = False
        while (k <= pow(log2_n, 2)):
            if ((pow(n, k)) % r == 1):
                flat = True
                break
            k += 1

        if (flat == False):
            output = r
            break

        r += 1
    return output


def euler_phi(r):
    output = r
    for i in range(2, int(math.sqrt(r)) + 1):
        if r % i == 0:
            while r % i == 0:
                r //= i  # //: chia làm tròn
            output -= output // i
    if r > 1:
        output -= output // r
    return output


def check_aks_in_rim(r, n):
    l = math.floor((2*math.sqrt(euler_phi(r))*math.log(n, 2) + 1))

    for a in range(1, l):
        # Khởi tạo một đối tượng s thuộc lớp Integers với modulo là n
        x = 'x'
        s = Integers(n)
        R = PolynomialRing(s, 'x')
        x = R.gen()
        F = R.quotient(x**r - 1)
        q = F(x + a)
        V = F(q**n)
        e = Mod(n, r)
        d = (x**e) + a
        if (V != d):
            print('n is composite')
            return

    print('n is prime')
    return


def aks_func(n):
    print(f'n = {n}')
    print('Step 1: check perfect power:')
    perfect_power = testing_for_perfect_power(n)
    if (perfect_power[0]):
        print('composite')
        print(
            f"n is perfect power n = {perfect_power[1]}^{perfect_power[2]}")
        return
    else:
        print('n is not perfect power')

    print('Step 2: find r:')
    r = find_an_appropriate_r(n)
    print(f'r = {r}')

    print('Step 3: check gcd(a, n)')
    for a in range(1, r):
        gcd_a_and_n = math.gcd(a, n)
        if (gcd_a_and_n > 1 and gcd_a_and_n < n):
            print(f'{n} is composite')
            return
        a += 1

    if (r >= n):
        print('n is prime')
        return
    
    print ('Step 4: check prime with r < n')
    check_aks_in_rim(r, n)


# istall
# 1. conda create --name sage_env
# 2. conda activate sage_env
# 3. conda config --add channels conda-forge
# 4. conda install sage
if __name__ == "__main__":
    # run with python3
    # n = 191502863810983023669487066171265783765606176368067317801145776531698322061026648391627756875377807727062582859038489434170143851401
    # n = 45884698721
    n = 4861
    aks_func(n)