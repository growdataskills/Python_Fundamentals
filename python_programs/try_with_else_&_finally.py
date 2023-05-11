try:
    i = int(input("Enter the value of i :"))
    c = 1/i
except Exception as e:
    print(e)
else:
    print("We were successfull.") #else only excute when there is no error in except block.

# -------------------------------------------------------------------------

try:
    i = int(input("Enter the value of i :"))
    c = 1/i
except Exception as e:
    print(e)
    # exit()
finally:
    print("We are done.") # finally excute regardless of error !

print("thanks.")