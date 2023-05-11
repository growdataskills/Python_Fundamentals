# Interchange 1st and last elments in a list.

def swap_method_1(list):
    n = len(list)
    list[0],list[n-1] = list[n-1],list[0]
    return list

def swap_method_2(list):
    a,*b,c = list
    list = [c,*b,a]
    return list

n = int(input("Enter the size :"))
list = []
for i in range (n):
    while True:
        try:
            element = int(input("enter the element : "))
            list.append(element)
            break
        except Exception as e :
            print("Please enter the number only.")

print("The normal way swapping")
print(swap_method_1(list))

print("swapping the element using * operands")
print(swap_method_2(list))