#Updating dictionary in same line.
#method 1:-
dict1 = {"abhaya" : 100, "rohit" : 200}
dict2 = {"abhinav" : 400, "rohan" : 300}

dict = {**dict1,**dict2}

print(dict)

#method 2:-
dict1 = {"abhaya" : 100, "rohit" : 200}
dict2 = {"abhinav" : 400, "rohan" : 300}
dict = {}
for i in (dict1,dict2):
    dict.update(i)

print(dict)