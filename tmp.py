from math import ceil, floor
from random import randint
import decimal


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def A(T, *, n):
    r = [0 for _ in range(10)]
    p = [0 for _ in range(10)]

    x0 = randint(1, 2**(n-1) - 1)
    c = randint(1, 2**(n-1) - 1)
    if c % 2 == 0:
        c += 1

    t = [T]

    i = 0
    while True:
        if t[i] >= n:
            a = int(floor(t[i] / 2))
            t.append(a)
            i += 1
        else:
            s = i
            break

    temp = int('1' + ''.join(['0' for _ in range(t[s] - 1)]), 2)
    while not is_prime(temp):
        temp += 1

    p[s] = temp

    m = s - 1
    r[m] = int(ceil(t[m + 1] / (n-1)))

    y = [x0] + [0 for _ in range(r[m])]

    print(t)
    while m >= 0:
        # print(m)
        while True:
            i = 1
            while i <= r[m]:
                y[i] = (97781173 * y[i - 1] + c) % 2 ** (n-1)
                i += 1

            Y = sum([k * 2**(n-1) for k in y[:-1]])
            y[0] = y[-1]
            # print(Y)
            a = (2**(t[m - 1])) / (p[m + 1])
            b = (2**(t[m - 1]) * Y) / ((p[m + 1]) * (2**((n-1) * r[m])))

            N = int(ceil(a)) + int(floor(b))
            if N % 2 == 1:
                N += 1

            k = 0
            while True:
                p[m] = p[m + 1] * (N + k) + 1
                # print(f'pm = {p[m]}; k = {k}')
                ch = p[m] > 2**t[m]
                # print(ch)
                if ch:
                    break
                f = (2**(p[m + 1] * (N + k))) % p[m] == 1
                s = (2**(N + k)) % p[m] != 1
                # print(f, s)
                if f and s:
                    break
                k += 2

            if p[m] <= 2**t[m]:
                m -= 1
                break
        p, q, *n = p

        return p, q


def C(p, q):
    d = randint(2, p - 2)
    k = int((p - 1) / q)
    f = 1
    while f == 1:
        f = (d**k) % p

    a = f
    return a

# print(t[5], p[5], p[4])
p, q = A(33, n=17)
print(p, q)
# print(*map(is_prime, (p, q)))
# print((p-1)/q)
# print(len(bin(p)[2:]))
# print(len(bin(q)[2:]))
a = C(p, q)
print(a)
