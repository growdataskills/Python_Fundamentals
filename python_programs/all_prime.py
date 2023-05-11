def series_prime(upper):
    print("Printing prime series to %d" %(upper))

    for num in range(upper + 1):
       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               print(num)
series_prime(int(input("Enter the number :")))
