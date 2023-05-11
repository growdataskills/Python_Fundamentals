square = lambda x : x*x
l = [1,2,3,4,5]

#map return the finale value of the list.
print("This is the map list.",list(map(square,l)))

#filter return the original value of an list.
print("This is the filter list.",list(filter(square,l)))