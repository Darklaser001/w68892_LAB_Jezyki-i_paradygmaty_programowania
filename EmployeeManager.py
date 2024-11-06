from idlelib.filelist import FileList

from Employee import Employee

class EmployeeManager(Employee):

    listOfEmployees = []

    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)

    def AddEmployee(self, name, age, salary):
        tmpEmployee = Employee(name, age, salary)
        self.listOfEmployees.append(tmpEmployee)

    def ShowEmployees(self):
        for Employee in self.listOfEmployees:
            print(Employee.view())

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

