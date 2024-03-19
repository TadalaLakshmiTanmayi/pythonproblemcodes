def test(n):
    if t == 0:
        return
    else:
        n = int(input())
        print(count(n))
    test(n-1)
def count(n):
    c = 0
    while n > 0:
        r = n%10
        if r == 4:
            c = c + 1
        n = n // 10
    return c
t = int(input())
test(t)