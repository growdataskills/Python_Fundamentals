# Passing Argument in a class.
class Foo():
    def __init__(self):
        self.variable = "Foo"
        print (self.variable) 

    def method(self, arg1, arg2):
        print ("in method (args):", arg1, arg2)

    def method2(self):
        self.method(3,4)


a = Foo()
a.method(1, 2)
a.method2()