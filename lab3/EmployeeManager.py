
from Employee import Employee

class EmployeeManager(Employee):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        self.listOfEmployees = []

    def AddEmployee(self, name, age, salary):
        tmpEmployee = Employee(name, age, salary)
        self.listOfEmployees.append(tmpEmployee)

    def ShowEmployees(self):
        for employee in self.listOfEmployees:
            print(employee.view())


    def DeleteEmployees(self, ageStart = -1, ageEnd = 999):
        if ageStart == ageEnd == -1:
            self.listOfEmployees.clear()

        for Employee in self.listOfEmployees:
                if Employee.age >= ageStart and Employee.age <= ageEnd:
                    self.listOfEmployees.remove(Employee)

    def FindEmployee(self, name):
        for Employee in self.listOfEmployees:
            if Employee.name == name:
                print(Employee.view())
                return Employee


    def UpdateSalary(self, name, salary):
        print("Przed aktualizacją")
        employeeSearched = self.FindEmployee(name)
        print("Po aktualizacji")
        employeeSearched.setSalary(salary)
        print(employeeSearched.view())

    
    def view(self):
        return f"Imię: \t{self.name}, wiek: \t{self.age}, salary \t{self.salary}"

