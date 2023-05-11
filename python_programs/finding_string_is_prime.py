def find_string_prime(word):
    n = len(word)
    print("The length of the string : ", n)

    prime = True
    for i in range (2,n):
        if (n%i == 0):
            prime = False
            break
    if prime:
        print("The string is prime.")
    else:
        print("The string is not prime.")

word = str(input("Enter a string :"))
find_string_prime(word)