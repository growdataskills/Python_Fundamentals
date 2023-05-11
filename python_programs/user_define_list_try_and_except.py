size = int(input("Enter the size of an arr : "))
arr = []

for i in range(size):
    while(True):
        try:
            Element = int(input("Enter the element %d : " %i))
            arr.append(Element)
            break
        except Exception as e:
            print("Your input reslt in an error.\n")
            print(e)

print(arr)