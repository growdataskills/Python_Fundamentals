#making an empty dictionary
#method 1
n = 3
d = dict(raw_input().split() for i in range(n))
print(d)

#method 2
#User Input Key and Value in a empty dictionary
size = int(input("Enter the size :"))
d = {}
for i in range(size):
    key = input("Enter the value for key:")
    value = input("Enter the value for value:")
    d[key] = value
print(d)