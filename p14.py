t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    if(a-c > b-d):
        print("2nd")
    elif(a-c < b-d):
        print("1st")
    else:
        print("any")
# discount