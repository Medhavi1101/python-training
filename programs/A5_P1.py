
class Circle:
    pass

def create(radius):
    c=Circle()
    c.radius=radius
    return c

def perimeter(c):
    if c.radius>0:
        return 2*(22/7)*c.radius

def area(c):
    if c.radius>0:
        return (22/7)*c.radius*c.radius

def info(c):
    return f'Circle<Radius: {c.radius}>' 

def draw(c):
    print(info(c))

def result_circle(radius):
    c=create(radius)
    draw(c)
    print(f'Area={area(c)}')
    print(f'Perimeter={perimeter(c)}')

result_circle(3)

