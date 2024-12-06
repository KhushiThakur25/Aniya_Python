class Employee:
    def __init__(self,name,emp_id,salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Id: {self.emp_id}")
        print(f"Salary: {self.salary}")


emp_1 = Employee("Ram",101,50000)
emp_2 = Employee("Riya",102,70000)

emp_2.display()


