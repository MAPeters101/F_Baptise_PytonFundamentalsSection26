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

class Point:
    def __init__(self, *coords):
        self.coordinates = coords
        print(f'dimension: {len(coords)}')

p = Point(1, 2)
print(p.__dict__)
print(p.coordinates)

p2 = Point(1,2,3,4,5)
print(p2.__dict__)
print(p2.coordinates)

class Circle:
    def __init__(self, *, radius=1):
        self.radius = radius

c = Circle()
print(c.radius)

c = Circle(radius=10)
print(c.radius)
print(vars(c))

class Circle:
    def __init__(self, *, radius=1):
        if radius <= 0:
            raise ValueError('Radius must be positive')
        self.radius = radius

c1 = Circle(radius=10)
print(vars(c1))

#c2 = Circle(radius=-1)


