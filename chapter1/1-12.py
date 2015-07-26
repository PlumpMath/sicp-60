

def pa(n):
    if n <= 1:
        return [1]

    row = [1]
    pre = pa(n - 1)
    for i, r in enumerate(pre[1:]):
        row.append(r + pre[i])
    row.append(1)
    return row


for i in range(10):
    print pa(i)

