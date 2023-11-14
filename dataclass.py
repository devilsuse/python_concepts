from dataclasses import dataclass

@dataclass
class Employee:
    name:str
    age:int
    dept:str

e = Employee('Rama',108,'divine')    
print(e.name + ' : ' + str(e.age) + ' : ' + e.dept)

'''
Traceback (most recent call last):
  File "c:/my/workspacePy/python_concepts/dataclass.py", line 23, in <module>
    em = Emp('Shyam', 5000, 'avatar')
TypeError: Emp() takes no arguments

class Emp:
    name:str
    age:int
    dept:str

em = Emp('Shyam', 5000, 'avatar')    
print(em.name + ' : ' + str(em.age) + ' : ' + em.dept)
'''