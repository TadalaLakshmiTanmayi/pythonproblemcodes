a=int(input())
b=int(input())
c=int(input())
if (a>b and a<c) or (a>c and a<b):
    print(a)
elif(b>c and b<a) or (b>a and b<c):
    print(b)
else:
    print(c)
#to print 2nd largest