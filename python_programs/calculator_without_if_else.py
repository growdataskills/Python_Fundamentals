import operator

action = {
    "+" : operator.add,
    "-" : operator.sub,
    "/" : operator.truediv,
    "*" : operator.mul,
    "**" : pow
}

num1 = int(input("Enter the num1 value : "))
num2 = int(input("Enter the num2 value : "))

operation = raw_input("Enter the operation : ")

print("The ans is", (action[operation](num1,num2)))