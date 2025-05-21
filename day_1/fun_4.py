# funkcja rekurencyjna - wywołuje samą siebie


def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)


print(silnia(5))


def nwd(a, b):
    if b == 0:
        return a
    return nwd(b, a % b)


print(nwd(48, 18))  # 6


def czy_pierwsza(n, dzielnik=2):
    if n < 2:
        return False
    if dzielnik * dzielnik > n:
        return True
    if n % dzielnik == 0:
        return False
    return czy_pierwsza(n, dzielnik + 1)

print(czy_pierwsza(29)) # True
print(czy_pierwsza(20)) # False