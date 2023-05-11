class details:
    def __init__(self,name,rollNo):
        self.name = name
        self.rollNo = rollNo

list = []
list.append(details("abhaya",151))
list.append(details("abha",152))
list.append(details("abh",153))

for i in list:
    print(i.name, i.rollNo)

# Also access instances attributes as list[0].name, list[0].roll and so on. 
print(list[1].name, list[1].rollNo)