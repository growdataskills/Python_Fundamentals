#simple iteration.
str = "banana"
myiter = iter(str)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#iteration using Class method.
class MyNumber():
    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if (self.num < 20):
            self.num += 1
            return self.num

        else:
            raise StopIteration

myclass = MyNumber()
myiter = iter(myclass)

for x in myiter:
    print(x)