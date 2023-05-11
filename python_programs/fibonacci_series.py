def fibonacci_number(num):
    f = 0
    s = 1
    for i in range(num + 1):
        if i <= 1:
            nxt = i
        else:
            nxt = f +s
            f = s
            s = nxt
        print (nxt)
print(fibonacci_number(int(input("Enter the number:"))))