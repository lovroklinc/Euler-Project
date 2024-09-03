def fibonaccci_list(seznam = [1, 1]):
    while True:
        if seznam[-1] >= 10 ** 999:
            return len(seznam) 
        else:
            seznam.append(seznam[-1] + seznam[-2])

print(fibonaccci_list())
