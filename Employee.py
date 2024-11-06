class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def view(self):
        return f"Imię: \t{self.name}, wiek: \t{self.age}, salary \t{self.salary}"

    def setSalary(self, salary):
        self.salary = salary