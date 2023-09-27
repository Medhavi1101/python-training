def sum( *args):
    result = 0
    for value in args:
        result += value
    return result
print(sum(1,2,3,4))


def average(*args):
    return sum(*args)/len(args)

print(average(1,2,3,4))

def call_me(x,y=10, *args):
    print(f'x={x}')
    print(f'y={y}')
    print(f'args={args}')

print(call_me(1,2,3))

def print_info(name, **kwargs):
    print(f'name = {name}')
    for key,value in kwargs.items():
        print(f'{key}= {value}')
print_info('Medhavi')


dict = {2:4, 11:6, 9:1, 7:3, 3:1}
def histogram(dict):
    for key,value in dict.items():
        print(f'{key}| {"+" * value * 5} {value}')

histogram(dict)