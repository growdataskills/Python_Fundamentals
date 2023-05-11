#for addition
class number():
    def __init__(self,num):
        self.num = num

    def __add__(self,num2):
        return(self.num + num2.num)

n = number(2)
n2 = number(2)
sum = n + n2
print(sum)

#---------------------------------------------------------------------------

#For Substraction

class number():
    def __init__(self,num):
        self.num = num

    def __sub__(self,num2):
        return(self.num - num2.num)

n = number(2)
n2 = number(2)
sub = n - n2
print(sub)

#---------------------------------------------------------------------------

#For Multiplication

class number():
    def __init__(self,num):
        self.num = num

    def __mul__(self,num2):
        return(self.num * num2.num)

n = number(2)
n2 = number(3)
mul = n * n2
print(mul)