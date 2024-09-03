def self_powers_to_n(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** i
    return sum
def last_n_digits(number, n):
    return number % (10 ** n)
print(last_n_digits(self_powers_to_n(1000), 10))