def multiples_of_n_below_k(n, k):
    mnozica = set()
    start = n
    while n < k:
        mnozica.add(n)
        n += start
    return mnozica
    
print(sum(multiples_of_n_below_k(3, 1000).union(multiples_of_n_below_k(5, 1000))))