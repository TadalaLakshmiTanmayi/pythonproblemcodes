class classn:
    def __init__(self,n):
        self.n=n
    def isprime(self):
        count=0
        for i in range(1,self.n+1):
            if self.n%i==0:
                count=count+1
        if count==2:
            return "yes"
        else:
            return "no"                
obj1=classn(20)
obj2=classn(12)
print(obj1.isprime())
print(obj2.isprime())
#isprime or not
#without parameter with return type print(obj1.isprime()) we have print here so we just need to return in method