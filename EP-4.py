def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def primes_smaller_than_n(n):
    list = []
    i = 2
    while i < n:
        if is_prime(i):
            list.append(i)
            i += 1
        else:
            i += 1
    return list

def biggest_power(n, m):
    start = n
    while n * start < m:
        n *= start
    return n

def all_nums_to_be_multiplied():
    list = []
    for i in primes_smaller_than_n(20):
        list.append(biggest_power(i, 20))
    return list

def result():
    product = 1
    for i in all_nums_to_be_multiplied():
        product *= i
    return product

print(result())



