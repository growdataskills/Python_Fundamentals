# User define set 

if __name__ == '__main__':
    lis = set()
    size = int(input("Enter the size : "))

    for i in range(size):
        element = int(input("Enter the element No. : %d " %(i+1)))
        lis.add(element)

    for i in lis:
        print(i,end=" ")