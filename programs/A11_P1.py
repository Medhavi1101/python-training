import time 
def performance_log(min, max):
    def prime_numbers(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        return inner
    return prime_numbers    

@performance_log(2,50)
def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

@performance_log(2,50)
def find_primes(min,max):
        start=time.time()
        primes=[]
        for x in range(min,max):
            if is_prime(x):
                primes.append(x)
            
        end=time.time()
        print(f'total time taken is {end-start}seconds')
        return primes

x = find_primes(2,50000)
print(len(x))

    