class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        print(f"Employee ID: {self.employee_id}\nName: {self.name}")

class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id)
        self.salary = salary
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Position: Manager\nSalary: {self.salary} RON \nDepartment: {self.department}")

    def organize_team_meeting(self):
        print("Organizing a team meeting.")

class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id)
        self.salary = salary
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Position: Engineer\nSalary: {self.salary} RON \nProgramming Language: {self.programming_language}")

    def write_code(self):
        print(f"{self.name} is writing code in {self.programming_language}.")

class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_target):
        super().__init__(name, employee_id)
        self.salary = salary
        self.sales_target = sales_target

    def display_info(self):
        super().display_info()
        print(f"Position: Salesperson\nSalary: {self.salary} RON\nSales Target: {self.sales_target} RON")

    def make_sale(self):
        print(f"{self.name} made a sale and reached the sales target.")

# Example usage
manager = Manager(name="Andrei Manager", employee_id=1, salary=80000, department="Marketing")
engineer = Engineer(name="Ramona Engineer", employee_id=2, salary=70000, programming_language="Python")
salesperson = Salesperson(name="Ionut Salesperson", employee_id=3, salary=60000, sales_target=100000)

manager.display_info()
manager.organize_team_meeting()
print()

engineer.display_info()
engineer.write_code()
print()

salesperson.display_info()
salesperson.make_sale()