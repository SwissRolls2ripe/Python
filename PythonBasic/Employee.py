class Employee:
	def __init__(self, name, emid):
		self.name = name
		self.emid = emid

	def print_info(self):
		print(f"Name: {self.name}, Employee ID: {self.emid}")

class FullTimeEmployee(Employee):
	def __init__(self, name, emid, monthly_salary):
		super().__init__(name, emid)
		self.monthly_salary = monthly_salary

	def calculate_monthly_pay(self):
		print(f"Monthly_salary: {self.monthly_salary}")

class PartTimeEmployee(Employee):
	def __init__(self, name, emid, daily_salary, work_days):
		super().__init__(name, emid)
		self.daily_salary = daily_salary
		self.work_days = work_days

	def calculate_monthly_pay(self):
		print(f"Monthly_salary: {self.daily_salary * self.work_days}")

Full_A = FullTimeEmployee("John Doe", 101, 5000)
print(f"{Full_A.name} {Full_A.emid} Full Time Employee Details:")
Full_A.calculate_monthly_pay()
Part_B = PartTimeEmployee("Jane Smith", 102, 200, 15)
print(f"{Part_B.name} {Part_B.emid} Part Time Employee Details:")
Part_B.calculate_monthly_pay()

