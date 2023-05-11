#Calender.
def calender(month,year):
    if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
	    print("Number of days are 31")
    elif ((month==2) and year%4==0):
	    print("Number of days are 28 and it is a leap year.")
    elif ((month==2)):
	    print("Number of days are 28.")
    else:
	    print("Number of days are 30.")
month = int(input("enter the monthe in digit :"))
year = int(input("enter the Year :"))
calender(month,year)