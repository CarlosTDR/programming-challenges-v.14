def bisiestos(i):
    res = 0
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            res = res + 1
    return res

i = int(raw_input())
print bisiestos(i)
