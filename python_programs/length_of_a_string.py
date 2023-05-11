#Finding length of a string in python.
def find_length(word):
    # return (len(word))
    count = 0
    for i in word:
        count+=1
    return count

word = str(input("Enter the string :"))
print(find_length(word))