def is_palindrome(n):
    length = len(str(n))
    n_list = [int(x) for x in str(n)]
    for i in range(int(length/2) + 1):
        if n_list[i] == n_list[-i -1]:
            pass
        else:
            return False
    return True

def main():
    list = []
    for a in range(100, 1000):
        for b in range(a, 1000):
            if is_palindrome(a * b):
                list.append(a * b)
    return list

print(max(main()))

