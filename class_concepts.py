class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

x = MyClass()
print(x.__doc__)

xf = x.f
#while True:
#    print(xf())