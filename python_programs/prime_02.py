num = int(input("Enter the Number :"))
prime = True
for i in range(2, num):
    if (num %i == 0):
        prime = False
        break
if prime:
    print("The number %d is a  prime number" %(num))
else:
    print("The number %d is not a  prime number" %(num))
