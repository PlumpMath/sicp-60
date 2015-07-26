

def cub(x):
    eps, y = 0.001, 1
    while True:
        if abs(y ** 3 - x) < eps:
            break
        else:
            y = (x/y**2 + 2*y)/3.0

    return y


def sqrt(x):
    return sqrt_iter(1.0, x)


def sqrt_iter(guess, x):
    if goot_enough(guess, x):
        return guess
    else:
        return sqrt_iter(improve(guess, x), x)


def goot_enough(guess, x):
    return abs(guess**2 - x) < 0.001


def improve(guess, x):
    return (guess + x/guess) / 2.0


print cub(10)
print cub(-10)
print cub(0)

print sqrt(10)
# print sqrt(-10)
# print sqrt(0)