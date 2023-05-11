while(True):
    print("Press q for quite :")
    a = (input("Enter a no.:"))
    if (a == 'q'): #always write if above the try statement to break the loop
        break
    try:
        print("Tring.....!!!!")
        a = int(a) # to check the input is a integer type or not.
        if (a>6):
            print("You enter a no. greater than 6.")
    except Exception as e:
        print("Your input reslt in an error.")