#finding triplets whoes sum is entered by the user.
def findTriplets(arr, n,sum): 
	for i in range(0, n-2): 
		for j in range(i+1, n-1): 
			for k in range(j+1, n): 
				if (arr[i] + arr[j] + arr[k] == sum): 
					print(arr[i], arr[j], arr[k])
                else: 
                    print(" not exist ") 
arr = [1, 5, 5, 2, 1] 
sum = 10
n = len(arr) 
findTriplets(arr, n,sum) 

#----------------------------------------------------------------------------

#finding triplets whoes sum is 0
def find_triplets(arr):
    n = len(arr)
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if (arr[i]+arr[j]+arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                else: 
                    print(" not exist ") 

arr = []
n = int(input("Enter the size :"))
for i in range(0,n):
    element = int(input("Enter the element No %d :" %(i+1)))
    arr.append(element)

print("Entered list is.")
for i in range(len(arr)):
    print(" %d " %(arr[i])),

find_triplets(arr)