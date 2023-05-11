def prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print ("the number %d is not a prime number" %(num))
                break;
        else:
            print (num,("is a prime number"))
    else:
        print ("This is not a prime number ",num)
prime (int(input("Enter the number:")))