class Dog:

    kind = 'canine'         # class variable shared by all instances
    tricks = []
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind + " : " + d.name)
print(e.kind + " : " + e.name)
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks) # unexpectedly shared by all dogs

#New attribute created below
d.counter = 1
while d.counter < 10:
    d.counter = d.counter * 2
    #print(e.counter) AttributeError: 'Dog' object has no attribute 'counter'
print(d.counter)
del d.counter
#print(d.counter) AttributeError: 'Dog' object has no attribute 'counter'

print('*******Class_and_instance_variable_name_conflict*********')
class Class_and_instance_variable_name_conflict:
    name = 'class_name'
    def __init__(self,name):
        self.name=name
    
    def display(self):
        print(name)
        
obj =   Class_and_instance_variable_name_conflict("Rama")
print(obj.name)

print('*******Object_created_without_parameter*********')
class Object_created_without_parameter:
    def __init__(self,name):
        self.name=name
    
    def display(self):
        print(self.name)
        
obj =  Object_created_without_parameter("Shyam")
print(obj.name)
obj.display()

print(' *******************  Function defined outside the class ***********')
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
p = C()  
print(type(p))  
print(p.g())

print('***Methods may call other methods by using method attributes of the self argument:******')
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)    
print(type(Bag))          

print('***isinstance() + issubclass(bool, int) :******')
print(isinstance(obj, int))
print(issubclass(bool, int))
print(issubclass(float, int))
