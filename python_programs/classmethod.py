#method 1:-
class employee():
    def __init__(self,salary):
        self.salary = salary

    @classmethod
    def changeSalary(cls,sal):
        return cls(sal)

    def income(self):
        print(self.salary)


e = employee(100)
e.income()

# e1 = e.changeSalary(500)
e1 = employee.changeSalary(500)
e1.income()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------

#method 2:-
# class employee():
#     salary = 100

#     def changeSalary(self,sal):
#         self.__class__.salary = sal

# e = employee()
# print(e.salary)

# e.changeSalary(500)
# print(e.salary)