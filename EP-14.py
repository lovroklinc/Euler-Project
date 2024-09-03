def naslednji_clen(n):
    if n%2== 0:
        return n//2
    else:
        return n*3 +1
    
def dolzina_zaporedja(n):
    k=1
    while n!=1:
        n=naslednji_clen(n)
        k +=1
    return k

def najdaljse_zaporedje(m, n):
    slovar = {1:1, }
    while m<=n:
        slovar[m] = dolzina_zaporedja(m)
        m +=1
    return max(slovar, key=slovar.get)
#made with usage of my already writen functions in TOMO
print(najdaljse_zaporedje(3, 1000000))
