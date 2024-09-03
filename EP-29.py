def main():
    mnozica = set()
    for a in range(2, 101):
        for b in range(2, 101):
            mnozica = mnozica.union({a ** b})
    return len(mnozica)

print(main())
