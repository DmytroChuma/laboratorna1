def factorial(n):
    i = 1
    a = 1
    while i <= n:
        a = a * i
        i = i + 1
    return a


b = int(input())
print(b,"! =", factorial(b))
