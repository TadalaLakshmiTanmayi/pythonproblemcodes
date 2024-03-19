t=int(input())
def test(t):
    if t>0:
        x,y=map(int,input().split())
        c=(x-y)+(y//2)
        print(c)
    else:
        return
    test(t-1)
test(t)