# coding: utf-8
#1美元换成50美分、25美分、10美分、5美分、1美分，一共有多少种方式

kinds = {1: 1, 2: 5, 3: 10, 4: 25, 5: 50}


def count_change(x, n):
    if x == 0:
        return 1
    elif x < 0 or n <= 0:
        return 0

    return count_change(x, n - 1) + count_change(x - kinds[n], n)

print count_change(100, 5)
