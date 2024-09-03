def sum_of_squares_under_n(n):
    sum = 0
    i = 1
    while i <= n:
        sum += i ** 2
        i += 1
    return sum

def sum_under_n_squared(n):
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1
    return sum ** 2

print(sum_under_n_squared(100) - sum_of_squares_under_n(100))
