#Swap two element by positions.
def swap(pos_1,pos_2,arr):
    arr[pos_1],arr[pos_2] = arr[pos_2],arr[pos_1]
    print(arr)


n = int(input("Enter the size :"))
arr = []
for i in range (n):
    while True:
        try:
            element = int(input("Enter the element :"))
            arr.append(element)
            break;
        except Exception as e:
            print(e)

pos_1 = int(input("Enter the postion for 1st element :"))
pos_2 = int(input("Enter the postion for 2nd element :"))

swap(pos_1,pos_2,arr)