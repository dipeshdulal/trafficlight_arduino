#learning about classes in python

# common class for all employees
# 
class Employee:
	'Documentation'
	empSalary = 0

	def __init__(self, salary):
		self.empSalary = salary
	def displaySalary(self):
		print("Your salary is",self.empSalary)

emp = Employee(5000)
emp.displaySalary()
