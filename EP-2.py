def fibonacci_gen():
    yield 1
    yield 2
    predzadnji = 1
    zadnji = 2
    while True:
        predzadnji, zadnji = zadnji, predzadnji + zadnji
        yield zadnji
#make a generator for the fibonacci sequence with which we can iterate

def solution():
    sum = 0
    for n in fibonacci_gen():
        if n % 2 == 0:
            sum += n
        if n > 4000000:
            break
    return sum

print(solution())



