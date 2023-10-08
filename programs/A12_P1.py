import time

def cached(func):
    cache = {}
    
    def inner(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return inner

def performance_monitor(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        time_taken = end_time - start_time
        print(f'{func.__name__} took {time_taken:.3f}')
        return result
    return inner

@cached
@performance_monitor
def factorial(n):
    fn = 1
    for i in range(1, n+1):
        time.sleep(0.5)
        fn *= i
    return fn

r1 = factorial(5)
r2 = factorial(7)
r3 = factorial(5)
print("Result 1: ", r1)
print("Result 2: ", r2)
print("Result 3: ", r3)
