class a:
    def display(self):
        pass
class b(a):
    def display(self):
        print("class b")
class c(a):
    def display(self):
        print("class c")
c1=c()
c1.display()
c2=b()
c2.display()