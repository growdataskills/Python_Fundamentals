#arithmatic series using recursion.
def find_the_nth(a,b,c,n):
    if n == a:
        return a
    elif n == b:
        return b
    elif n == c:
        return c
    else:
        return (n-1)+(n-2)+(n-3)
a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
c = int(input("Enter the value of c :"))
n = int(input("Enter the value of n :"))
a = (find_the_nth(a,b,c,n))
print("The ans is",a)