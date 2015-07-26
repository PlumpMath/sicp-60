
def f1(n):
    if n == 1: return 1
    elif n == 2: return 2
    elif n == 3: return 3

    return f1(n-1) + 2*f1(n-2) + 3*f1(n-3)


def f2(n):
    a, b, c = 1, 2, 3
    while True:
        if n - 1 <= 0:
            return a

        a, b, c = b, c, c + 2 * b + 3 * a
        n -= 1


for i in range(1, 10):
    print f1(i), f2(i)