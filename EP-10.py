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
#from problem 7

def sum_primes_below_n(n):
    list = [0]
    for i in prime_generator():
        if i < n:
            list.append(i)
        else:
            return sum(list)
#works really slowly and inefficiently but it works

print(sum_primes_below_n(2000000))

