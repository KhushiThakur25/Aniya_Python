class Employee:
    def __init__(self,name,emp_id,salary):
        self.name = name
        self.emp_id = emp_id
        self.__salary = salary #private
#public, private , _ - protected 
    def getter(self):
        return self.__salary

    def setter(self,new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary amount..")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Id: {self.emp_id}")
        print(f"Salary: {self.__salary}")

emp_1 = Employee("Ram",101,50000)
emp_2 = Employee("Riya",102,70000)

emp_1.setter(60000)
print(emp_1.getter())

        
