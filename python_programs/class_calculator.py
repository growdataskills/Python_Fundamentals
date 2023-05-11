class calculator:
    def __init__(self,num):
        self.number = num
    def square(self):
        print("the value of square is %d" %(self.number**2))
    def squareRoot(self):
        print("the value of square root is %d" %(self.number**0.5))
    def cube(self):
        print("the value of cube is %d" %(self.number**3))
    
    @staticmethod
    def greet():
        print("thanks for calculating.")


a = calculator(2)
a.square()
a.squareRoot()
a.cube()
a.greet()