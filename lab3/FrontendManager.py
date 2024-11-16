import json
from EmployeeManager import *


def mainMenu(managerList, managerChosen):
    manager = managerList[managerChosen]
    
    while True:
        print("0. Wyjdź")
        print("1. Dodaj nowego pracownika")
        print("2. Wyświetl listę pracowników")
        print("3. Usuń pracownika")
        print("4. Zmień wynagrodzenie")
        print("5. Zapisz zmiany")
        print("6. Zmień kierownika")
        print("7. Dodaj nowego kierownika")
        print("8. Usuń menedżera")
        print("9. Edytuj menedżera")
        
        choice = input("Wybierz opcję: ")
        
        if not choice.isdigit():
            print("Nieprawidłowy wybór! Proszę podać liczbę.")
            continue
        
        choice = int(choice)
        
        if choice == 0:
            exit(72)
        
        elif choice == 1:
            name = input("Podaj imię: ")
            while not name.strip():
                print("Imię nie może być puste!")
                name = input("Podaj imię: ")
                
            age = input("Podaj wiek: ")
            while not age.isdigit() or int(age) <= 0:
                print("Wiek musi być liczbą całkowitą większą niż 0!")
                age = input("Podaj wiek: ")
            age = int(age)
            
            salary = input("Podaj wynagrodzenie: ")
            while not salary.isdigit() or int(salary) < 0:
                print("Wynagrodzenie musi być liczbą całkowitą większą lub równą 0!")
                salary = input("Podaj wynagrodzenie: ")
            salary = int(salary)
            
            manager.AddEmployee(name, age, salary)
        
        elif choice == 2:
            manager.ShowEmployees()
        
        elif choice == 3:
            startAge = input("Podaj początek przedziału: ")
            while not startAge.isdigit():
                print("Wiek musi być liczbą całkowitą!")
                startAge = input("Podaj początek przedziału: ")
            startAge = int(startAge)
            
            endAge = input("Podaj koniec przedziału: ")
            while not endAge.isdigit() or int(endAge) < startAge:
                print("Koniec przedziału musi być liczbą całkowitą i większy lub równy początkowi!")
                endAge = input("Podaj koniec przedziału: ")
            endAge = int(endAge)
            
            manager.DeleteEmployees(startAge, endAge)
        
        elif choice == 4:
            name = input("Podaj imię pracownika: ")
            while not name.strip():
                print("Imię nie może być puste!")
                name = input("Podaj imię pracownika: ")
                
            salary = input("Podaj nowe wynagrodzenie: ")
            while not salary.isdigit() or int(salary) < 0:
                print("Wynagrodzenie musi być liczbą całkowitą większą lub równą 0!")
                salary = input("Podaj nowe wynagrodzenie: ")
            salary = int(salary)
            
            manager.UpdateSalary(name, salary)
        
        elif choice == 5:
            assurance = input("Czy jesteś pewny zmian? (Y/N): ")
            if assurance == 'Y' or assurance == 'y':
                saveData(managerList, 'employees.json')
        
        elif choice == 6:
            managerIndex = input("Wybierz managera (0,1,2,3....): ")
            while not managerIndex.isdigit() or int(managerIndex) < 0 or int(managerIndex) >= len(managerList):
                print("Nieprawidłowy numer menedżera!")
                managerIndex = input("Wybierz managera (0,1,2,3....): ")
            managerChosen = int(managerIndex)

        elif choice == 7:
            name = input("Podaj imię nowego menedżera: ")
            while not name.strip():
                print("Imię menedżera nie może być puste!")
                name = input("Podaj imię nowego menedżera: ")
                
            age = input("Podaj wiek menedżera: ")
            while not age.isdigit() or int(age) <= 0:
                print("Wiek menedżera musi być liczbą całkowitą większą niż 0!")
                age = input("Podaj wiek menedżera: ")
            age = int(age)
            
            salary = input("Podaj wynagrodzenie menedżera: ")
            while not salary.isdigit() or int(salary) < 0:
                print("Wynagrodzenie menedżera musi być liczbą całkowitą większą lub równą 0!")
                salary = input("Podaj wynagrodzenie menedżera: ")
            salary = int(salary)
            
            newManager = EmployeeManager(name, age, salary)
            managerList.append(newManager)
            
            print(f"Nowy menedżer {name} został dodany.")

        elif choice == 8:
            managerIndex = input("Wybierz menedżera do usunięcia (0, 1, 2, ...): ")
            while not managerIndex.isdigit() or int(managerIndex) < 0 or int(managerIndex) >= len(managerList):
                print("Nieprawidłowy numer menedżera!")
                managerIndex = input("Wybierz menedżera do usunięcia (0, 1, 2, ...): ")
            managerIndex = int(managerIndex)
            del managerList[managerIndex]
            print("Menedżer został usunięty.")
        
        elif choice == 9:
            managerIndex = input("Wybierz menedżera do edytowania (0, 1, 2, ...): ")
            while not managerIndex.isdigit() or int(managerIndex) < 0 or int(managerIndex) >= len(managerList):
                print("Nieprawidłowy numer menedżera!")
                managerIndex = input("Wybierz menedżera do edytowania (0, 1, 2, ...): ")
            managerIndex = int(managerIndex)
            
            name = input(f"Podaj nowe imię dla menedżera {managerList[managerIndex].name}: ")
            while not name.strip():
                print("Imię nie może być puste!")
                name = input(f"Podaj nowe imię dla menedżera {managerList[managerIndex].name}: ")
            managerList[managerIndex].name = name
            
            age = input(f"Podaj nowy wiek dla menedżera {managerList[managerIndex].name}: ")
            while not age.isdigit() or int(age) <= 0:
                print("Wiek musi być liczbą całkowitą większą niż 0!")
                age = input(f"Podaj nowy wiek dla menedżera {managerList[managerIndex].name}: ")
            managerList[managerIndex].age = int(age)
            
            salary = input(f"Podaj nowe wynagrodzenie dla menedżera {managerList[managerIndex].name}: ")
            while not salary.isdigit() or int(salary) < 0:
                print("Wynagrodzenie musi być liczbą całkowitą większą lub równą 0!")
                salary = input(f"Podaj nowe wynagrodzenie dla menedżera {managerList[managerIndex].name}: ")
            managerList[managerIndex].salary = int(salary)
            
            print("Dane menedżera zostały zaktualizowane.")
        
        input("Wciśnij enter by kontynuować")


def logIn():
    if input("Podaj login: ") == "Admin" and input("Podaj hasło: ") == "Admin":
        return True
    return False


def saveData(listOfManagers, filePath):
    data = {"managers": []}
    
    for manager in listOfManagers:
        managerData = {
            "name": manager.name,
            "age": manager.age,
            "salary": manager.salary,
            "employees": []
        }

        for employee in manager.listOfEmployees:
            employeeData = {
                "name": employee.name,
                "age": employee.age,
                "salary": employee.salary
            }
            managerData["employees"].append(employeeData)

        data["managers"].append(managerData)

    with open(filePath, 'w') as file:
        json.dump(data, file, indent=4)
