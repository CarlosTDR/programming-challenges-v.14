
def bisiestos(i,j):
    res = 0
    for i in range(i,j):
        if i%4 == 0 and (i%100 != 0 or i%400 == 0):
            res = res + 1
    return res

i = int(raw_input())
j = int(raw_input())
print bisiestos(i,j)
