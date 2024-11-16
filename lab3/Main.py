from Vehicle import Car
from abc import ABC, abstractmethod
from EmployeeManager import *
from FrontendManager import *
from Employee import *
import json

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Lion(Animal):
    def sound(self):
        return f"Rawr"

# lion = Lion()
# print(lion.sound())
#
# car1 = Car("Skoda","Octavia","2010")
# print(car1.description())

listOfManagers = []

def loadData():
    with open('employees.json', 'r') as file:
        data = json.load(file)

        for manager in data['managers']:

            managerEmployee = EmployeeManager(manager['name'], manager['age'], manager['salary'])

            for employee in manager['employees']:
                managerEmployee.AddEmployee(employee['name'], employee['age'], employee['salary'])
            
            listOfManagers.append(managerEmployee)




loggedIn = True

while(not loggedIn):
    logIn()



loadData()
for manager in listOfManagers:
    print(manager.view())
managerChosen = int(input("Wybierz managera (0,1,2,3....): "))
mainMenu(listOfManagers, managerChosen)



