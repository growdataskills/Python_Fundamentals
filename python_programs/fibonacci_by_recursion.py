def fibonacci_number(num):
    if num == 1 or num == 2:
        return 1
    else:
        return (fibonacci_number(num - 1)+fibonacci_number(num - 2))
print(fibonacci_number(int(input("Enter the number:")))