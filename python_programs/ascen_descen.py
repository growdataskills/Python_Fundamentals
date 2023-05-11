#Ascending descening of list.
arr = []
n = int(input("Enter the size:"))
for i in range(0,n):
    element = int(input("Enter the elemen No. %d:" %(i+1)))
    arr.append(element)
print("\nEntered List is.")
for i in range(len(arr)):
    print("%d" %(arr[i]))
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[j]<arr[i]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print("\nArranged List is.")
for i in range(len(arr)):
    print("%d" %(arr[i]))