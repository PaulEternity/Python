n,m = map(int,input().split())

if m < n:
    print(0.0000)
else:
    num = 1 - pow((n - 1) / n, m - 1)

    result = "{:.4f}".format(num)

    print(result)

