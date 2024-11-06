from Vehicle import Car
from abc import ABC, abstractmethod
from EmployeeManager import *
from FrontendManager import *

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

jurek = EmployeeManager("Jurek", 72, 100)
jurek.AddEmployee("Zbychu", 52, 70)
jurek.AddEmployee("Janusz", 70, 80)
jurek.AddEmployee("Mariolka", 25, 60)
jurek.AddEmployee("Dariusz", 47, 75)
jurek.AddEmployee("Jezus", 33, -10)

loggedIn = False
while(True):
    if(loggedIn):
        mainMenu(jurek)
    else:
        loggedIn = logIn()


