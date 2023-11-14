class Square:
    def __init__(self, length, color=None):
        self.length=length
        self.color=color

    def __repr__(self):
        return f"Square({self.length!r}, {self.color!r})"

    @property
    def area(self):
        return self.length**2

s1=Square(4)        
print(s1)

print(s1.area)

s1.length=3
print(s1.area)
