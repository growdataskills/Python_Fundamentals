def calculate(num1,num2,i):
    switcher={
        1 : num1+num2,  
        2 : num1-num2, 
        3 : num1*num2, 
        4 : num1/num2,
    }
    return switcher.get(i,"Invalid selection")
num1 = int(input("Enter the value for num1:"))
num2 = int(input("Enter the value for num2:"))
print("Enter 1 for addition.")
print("Enter 2 for substraction.")
print("Enter 3 for multiplication.")
print("Enter 4 for division.")
operation = int(input("Enter the value for op:"))
ans = calculate(num1,num2,operation)
if operation == 1:
    operation = '+'
elif operation == 2:
    operation = '-'
elif operation == 3:
    operation = '*'
else:
    operation = '/'
print("The ans of {a} {c} {b} is {d}".format(a = num1,b = num2,c = operation,d = ans))