from math import sqrt
class Triangle:
    pass
def create(s1,s2,s3):
    t=Triangle()
    t.s1=s1
    t.s2=s2
    t.s3=s3
    return t
def is_valid(t):
    return isinstance(t,Triangle ) and \
        t.s1>0 and t.s2>0 and t.s3>0 and \
        t.s1+t.s2 > t.s3 and \
        t.s2+t.s3 > t.s1 and \
        t.s1+t.s3 > t.s2
def perimeter(t):
    return t.s1+t.s2+t.s3 if is_valid(t) else float('nan')

def area(t):
    if is_valid(t):
        s=perimeter(t)/2
        sqrt(s*(s-t.s1)*(s-t.s2)*(s-t.s3))

def info(t):
    return f'Triangle<{t.s1},{t.s2},{t.s3}>' if is_valid(t) else '<Invalid Triangle>'

def draw(t):
    print(info(t))

def test_triangle(s1,s2,s3):
    t=create(s1,s2,s3)
    draw(t)
    if is_valid(t):
        print(f'Area={area(t)}')
        print(f'Perimeter={area(t)}')

test_triangle(3,4,5)

