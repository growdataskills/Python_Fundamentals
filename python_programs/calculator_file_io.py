def calculation (num1,num2,i):
    switcher = {
        1 : num1 + num2,
        2 : num1 - num2,
        3 : num1 * num2,
        4 : num1 / num2,
    }
    return switcher.get(i,"Invalid selection")

num1 = int(input("Enter the value for num1 :"))
num2 = int(input("Enter the value for num2 :"))

print("Enter 1 for addition.")
print("Enter 2 for substraction.")
print("Enter 3 for multiplication.")
print("Enter 4 for division.")

operation = int(input("Enter the value for op:"))

ans = calculation(num1,num2,operation)

if operation == 1:
    operation = '+'
    with open("sample.txt","a") as f:
        f.write("\nThe ans of {a} {c} {b} is {d}".format(a = num1,b = num2,c = operation,d = ans))

elif operation == 2:
    operation = '-'
    with open("sample.txt","a") as f:
        f.write("\nThe ans of {a} {c} {b} is {d}".format(a = num1,b = num2,c = operation,d = ans))

elif operation == 3:
    operation = '*'
    with open("sample.txt","a") as f:
        f.write("\nThe ans of {a} {c} {b} is {d}".format(a = num1,b = num2,c = operation,d = ans))

else:
    operation = '/'
    with open("sample.txt","a") as f:
        f.write("\nThe ans of {a} {c} {b} is {d}".format(a = num1,b = num2,c = operation,d = ans))

print("The ans of num1:{a} {c} num2:{b} is {d}".format(a = num1,b = num2,c = operation,d = ans))

print("If you want to see your history then type (y) for Yes and (n) For No :")
print("If you want to delete your history then type (d) for delete:")
select = raw_input("Enter y/n/d:")

if select == "y":
    with open("sample.txt",) as f:
        content = f.read()
        print(content)

elif select == "n":
    print("Exiting the program thanks for using me .")
    exit()

elif select == "d":
    with open("sample.txt","w") as f:
        f.write("")
else:
    print("Invalid Selection.........")
