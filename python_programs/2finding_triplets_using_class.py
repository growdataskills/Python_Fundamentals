#Method 1: passing list in the class.
class zeroTriplets:
    def __init__(self,arr):
        self.arr = arr

    def threeSum(self):
        n = len(self.arr)
        for i in range(0, n-2): 
            for j in range(i+1, n-1): 
                for k in range(j+1, n): 
                    if (self.arr[i] + self.arr[j] + self.arr[k] == 0): 
                        print(self.arr[i], self.arr[j], self.arr[k])
                    # else: 
                    #     print(" not exist ") 

class display_arr(zeroTriplets):
    def print_list(self):
        print(self.arr)

list1 = [-25, -10, -7, -3, 2, 4, 8, 10]
a = zeroTriplets(list1)
a.threeSum()

b = display_arr(list1)
b.print_list()

#------------------------------------------------------------------------------------------------

#method 2:passing list to the function in the class.
class py_solution:
    def threeSum(self, arr):
        n = len(arr)
        for i in range(0, n-2): 
            for j in range(i+1, n-1): 
                for k in range(j+1, n): 
                    if (arr[i] + arr[j] + arr[k] == 0): 
                        print(arr[i], arr[j], arr[k])
                    # else: 
                    #     print(" not exist ") 

# method 1:-
a = py_solution()
a.threeSum([-25, -10, -7, -3, 2, 4, 8, 10])

# method 2:-
py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10])