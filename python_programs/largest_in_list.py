#largest in a list.
arr = []
n = int(input("Enter the size:"))
for i in range(0,n):
    element = int(input("Enter the elemen No. %d:" %(i+1)))
    arr.append(element)
for i in range(len(arr)):
    print("%d" %(arr[i]))
largest = arr[0]
for i in range(len(arr)):
    if (largest < arr[i]):
        largest = arr[i]
print("largest element present in the given array is : %d" %(largest));