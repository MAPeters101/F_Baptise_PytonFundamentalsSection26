class Person:
    """This string can be used to document this class -
    called a docstring"""

p1 = Person()
print(p1)
print(p1.__doc__)

print(help(Person))
print(Person.__name__)
print(p1.__class__)
print(p1.__class__ is Person)
print(type(p1))
print(type([1,2,3]) is list)
print(type(p1) is Person)


a = 1
print(isinstance(a, int))
print(type(a) is int)
print(isinstance(p1, Person))
print(type(p1) is Person)

p1.name = 'John'
print(p1.name)

a = 100
#a.name = 'hunmdred'

def hello():
    pass

hello.name = 'says hello'
print(hello.name)
