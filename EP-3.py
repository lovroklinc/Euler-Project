def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    k = 3
    while k ** 2 <= n:
        while n % k == 0:
            factors.append(k)
            n = n // k
        k += 2   
    if n > 2:
        factors.append(n)
    return factors

print(max(prime_factors(600851475143)))