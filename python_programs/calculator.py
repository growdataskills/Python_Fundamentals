#Simple calculator
def add(x,y):
    return x+y
def subs(x,y):
    return x-y
def multi(x,y):
    return x*y
def divide(x,y):
    return x/y
    
num1 = int(input("Enter the Value of Num1 :"))
num2 = int(input("Enter the Value of NUm2 :"))

print("Choose 1 for '+'/ 2 for '-'/ 3 for '*'/ 4 for '/' :-")
select = int(input("Enter the 1/2/3/4 :"))

if select == 1 :
    print(num1,"+",num2,"=",add(num1,num2))
elif select == 2 :
    print(num1,"-",num2,"=",subs(num1,num2))
elif select == 3 :
    print(num1,"*",num2,"=",multi(num1,num2))
elif select == 4 :
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("Enter the Valid number.")
