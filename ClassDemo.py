class MyClass:
    i=1234

    def f(self):
        return "Hare Rama !"

x=MyClass()
print(__name__)
print(x.i)
print(x.__doc__)

class Complex:
    def __init__(self, real, im):
        self.r=real
        self.i=im

c=Complex(3.0,-4.5)
print(c.r,c.i)
c.counter =1
while c.counter < 10:
    c.counter *= 2
print(c.counter)
del c.counter
#print("After deleting counter attr", c.counter)