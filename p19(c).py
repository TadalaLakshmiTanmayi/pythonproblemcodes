#sugarcane juice business--codchef approach 4
t=int(input())
def profit(n):
    x=(int)((n*50)-((0.7)*(n*50)))
    return x
def test(t):
    if t>0:
        n=int(input())
        print(profit(n))
    else:
        return
    test(t-1)
test(t)