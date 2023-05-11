def fact(n):
    if n > 0:
        return (n*fact(n - 1))
    else:
        return 1
print(fact(5))
