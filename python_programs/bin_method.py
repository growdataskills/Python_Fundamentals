# bin() method takes a single parameter:
# bin() method returns the binary string equivalent to the given integer.

number = 5
print('The binary equivalent of 5 is:', bin(number))

#----------------------------------------------------------------------------

class Quantity:
    apple = 1
    orange = 2
    grapes = 2
    
    def __index__(self):
        return self.apple + self.orange + self.grapes
        
print('The binary equivalent of quantity is:', bin(Quantity()))