import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, ex_type, ex_obj, ex_stack):
        self.end_time = time.time()
        self.time_taken = self.end_time - self.start_time


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


def find_primes(min,max):
        primes=[]
        for x in range(min,max):
            if is_prime(x):
                primes.append(x)
        return primes


with Timer() as t:
    primes = find_primes(2,20000)

time_taken = t.time_taken

print("Total primes: ", len(primes))
print("Total time taken: ", time_taken)
            



