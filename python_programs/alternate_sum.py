#alternate sum.
arr = []
n = int(input("Enter the size :"))
for i in range(0,n):
    element = int(input("Enter the Element no. {} :".format(i+1)))
    arr.append(element)
size = len(arr)
for i in range(size):
    print(" {}".format(arr[i]))
print("The alternate sum.") 
print("The original list : " + str(arr)) 
res = [sum(arr[i : : 2]) for i in range(len(arr)//(len(arr)//2))] 
# print result 
print("The alternate elements summation list :" + str(res))
print("\n") 