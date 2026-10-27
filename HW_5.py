def is_prime(n):
    if n <= 1:
        return False
        
    if n == 2:
        return True
        
    if n % 2 == 0:
        return False
        
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
            
    return True


def is_fib(num):
    l = [0, 1]
    term = 0
    for i in range(2, num):
        term = l[i-1] + l[i-2]
        l.append(term)
    return l

num = int(input())
print(is_prime(num))

#print(is_fib(10))
