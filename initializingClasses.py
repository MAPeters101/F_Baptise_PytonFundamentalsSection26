class Person:
    """Class to represent a Person"""

p1 = Person()
print(p1, type(p1))
print(hex(id(p1)))

class Person:
    def __init__(self):
        print('custom init...')

p = Person()

class Person:
    def __init__(self):
        print('custom init...', self)

p1 = Person()
print(hex(id(p1)))


p1 = Person()
p1.first_name = 'Eric'
p1.last_name = 'Idle'
print(p1.__dict__)

class Person:
    def __init__(self):
        self.first_name = 'Eric'
        self.last_name = 'Idle'

p1 = Person()
print(p1.__dict__)
print(p1.first_name, p1.last_name)
print('-'*10)


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

#p1 = Person()
p1 = Person('Eric', 'Idle')
print(p1.__dict__)
print(p1.first_name, p1.last_name)

print('+'*10)

p1 = Person('John', 'Cleese')
print(p1.__dict__)
print(p1.first_name, p1.last_name)

print('='*10)

