#find single duplicate element in array-Hackerrank
n=int(input())
a=0
l=list(map(int,input().split()))
for j in range(n):
    if(l[j-1]==l[j]):
        a=l[j]
        break
print(a)