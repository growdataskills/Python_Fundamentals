class employee():
    salary = 100
    salaryBonus = 200

    @property
    def totalsalary(self):
        # print(self.salary + self.salaryBonus)
        return(self.salary + self.salaryBonus)

    @totalsalary.setter
    def totalsalary(self,value):
        self.salaryBonus = value - self.salary

e = employee()
# e.totalsalary

print("Total salaray of an employee",+e.totalsalary)
print("Salary of an employee is", + e.salary)
print("Salary after bonus is", +e.salaryBonus)

e.totalsalary = 400

print("Salary of an employee is", +e.salary)
print("New salary bonus is",+e.salaryBonus)