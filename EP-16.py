def sum_digits(n):
    sum = 0
    if n < 10:
        sum += n
    else:
        sum = (n % 10) + sum_digits(n // 10)
    return sum

print(sum_digits(2 ** 1000))

