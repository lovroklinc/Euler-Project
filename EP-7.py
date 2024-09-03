def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True
#from problem 5

def prime_generator():
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 1
    
def nth_prime(n):
    list = []
    for i in prime_generator():
        if len(list) < n:
            list.append(i)
        elif len(list) == n:
            return max(list)
print(nth_prime(10001))