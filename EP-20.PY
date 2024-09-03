def sum_digits(n):
    sum = 0
    if n < 10:
        sum += n
    else:
        sum = (n % 10) + sum_digits(n // 10)
    return sum
#from problem 16

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
    
print(sum_digits(factorial(100)))