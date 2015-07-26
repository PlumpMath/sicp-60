

def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1

    return a


def fib2(n):
    if n <= 1 or n == 2:
        return 1

    return fib2(n-1) + fib2(n-2)

for i in range(1, 20):
    print fib(i), int(((1+5**0.5)/2)**i/5**0.5)

for i in range(1, 20):
    print fib2(i),
