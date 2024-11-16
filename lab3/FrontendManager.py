def mainMenu(jurek):
    print("0. Wyjdź")
    print("1. Dodaj nowego pracownika")
    print("2. Wyświetl listę pracowników")
    print("3. Usuń pracownika")
    print("4. Zmień wynagrodzenie")
    choice = int(input("Wybierz opcję:"))
    if choice == 0:
        exit(72)
    elif choice == 1:
        jurek.AddEmployee(input("Podaj imię: ", int(input("Podaj wiek: ")), int(input("Podaj wynagrodzenie: "))))
    elif choice == 2:
        jurek.ShowEmployees()
    elif choice == 3:
        jurek.DeleteEmployees(int(input("Podaj początek przedziału: ")), int(input("Podaj koniec przedziału: ")))
    elif choice == 4:
        jurek.UpdateSalary(input("Podaj imię pracownika: "), int(input("Podaj nowe wynagrodzenie: ")))

def logIn():
    if input("Podaj login: ") == "Admin" and input("Podaj hasło: ") == "Admin":
        return True
    return False
