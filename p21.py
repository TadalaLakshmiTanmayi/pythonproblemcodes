t=int(input())
for i in range(t):
    n=int(input())
    count=0
    while n>0:
        if(n%10==4):
            count=count+1
        n=n//10
    print(count)
    # number of 4s