#sugarcane juice business--codchef approach 3
t=int(input())
def test(t):
    if t>0:
        n=int(input())
        x=(int)((n*50)-((0.7)*(n*50)))
        print(x)
    else:
        return 
    test(t-1)
test(t)