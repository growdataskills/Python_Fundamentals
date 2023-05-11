#Adding to numbers using class.
class details:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def sum(self):
        print(self.x + self.y)

list = []
list.append(details(1,2))
list.append(details(3,4))
list.append(details(5,6))

for i in list:
    i.sum()

print("\n")

# Also access instances attributes as list[0].name, list[0].roll and so on. 
list[1].sum()
list[2].sum()