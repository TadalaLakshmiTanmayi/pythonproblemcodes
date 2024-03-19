#reverse
num=int(input())
reversed_num = 0
if(num>0):
    sign=1

else:
    sign=-1

num1=abs(num)
while num1 != 0:
    digit = num1 % 10
    reversed_num = reversed_num * 10 + digit
    num1 //= 10
reversed_num *= sign
print(reversed_num)
