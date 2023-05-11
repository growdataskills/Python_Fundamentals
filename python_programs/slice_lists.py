# Remember that you can slice lists!
# list_name[startAt:endBefore:skip]
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for _ in my_list[::2]
    print(_,end=" ")
    
# Output: 1 3 5 7 9