def pythagorean_triplet(a,b,c):
    value = (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (c ** 2 + b ** 2 == a ** 2)
    return value
    
def result():
    sum = 1000
    max_a = sum // 3 #because b and c have to be bigger than a
    for a in range(1, max_a):
        for b in range(a, (sum - a) // 2):
            c = sum - a - b
            if pythagorean_triplet(a, b, c):
                return a * b * c
            
print(result())