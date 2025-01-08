type Person(name: string, age: int) =
    // private variables
    let mutable privateAge = age

    //public variables
    //val mutable public surname:string

    // properties
    member this.Name = name

    // getters/setters
    member this.Age
        with get() = privateAge
        and set(value) =
            if value > 0 then
                privateAge <- value
            else
                printfn "Wiek musi być większe od zera!"


    // methods
    member this.View() =
        printfn "Witaj %s masz %d lat." this.Name this.Age



// derived class / subclass
type Student(name:string, age:int, nrAlbumu: string) =
    inherit Person(name,age)

    //properties
    member this.NrAlbumu = nrAlbumu

    override this.View() = 
        printfn "Witaj %s masz %d lat. Twój numer albumu to %s" this.Name this.Age this.NrAlbumu






// class object

let person = Person("Jan", -1)
person.View()
let student = Student("Izbeski", 12, "w69420")
student.View()