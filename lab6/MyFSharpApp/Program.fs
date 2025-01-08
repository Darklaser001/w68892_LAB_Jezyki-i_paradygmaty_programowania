// book

open System

type Book(title: string, author: string, pages: int) =
    member this.Title = title
    member this.Author = author
    member this.Pages = pages

    // methods
    member this.GetInfo() =
        sprintf "Tytuł: %s. Autor: %s. Liczba stron: %d" this.Title this.Author this.Pages

// user

type User(name: string) =
    
    let borrowBooks = System.Collections.Generic.List<Book>()
    member this.Name = name

    member this.BorrowBook(book: Book) =
        borrowBooks.Add(book)
        printfn "%s wypożyczył książkę \"%s\"" this.Name book.Title

    member this.ReturnBook(book: Book) =
        if borrowBooks.Contains(book) then
            borrowBooks.Remove(book)
            printfn "%s zwrócił książkę \"%s\"" this.Name book.Title
        else
            printfn "%s nie ma takiej książki w wypożyczonych" this.Name

    member this.ListBorrowBooks() =
        if borrowBooks.Count > 0 then
            borrowBooks
            |> Seq.map (fun book -> book.GetInfo())
            |> String.concat "\n"
            |> printfn "Książki wypożyczone przez %s:\n%s" this.Name
        else 
            printfn "%s nie ma wypożyczonych książek"  this.Name


type Library() =
    let mutable books = System.Collections.Generic.List<Book>()

    member this.AddBook(book: Book) =
        books.Add(book)
        printfn "Książka \"%s\" została dodana do biblioteki" book.Title

    member this.RemoveBook(book: Book) =
        if books.Contains(book) then
            books.Remove(book)
            printfn "Książka \"%s\" została usunięta z biblioteki" book.Title
        else
            printfn "Nie znaleziono książki"

    member this.ListOfBooks() =
        if books.Count > 0 then
            books
            |> Seq.map (fun book -> book.GetInfo())
            |> String.concat "\n"
            |> printfn "Książki w bibliotece: \n%s"
        else 
            printfn "W bibliotece nie ma książek"

let main() =
    let library = Library()
    let user = User("Jan")

    let book1 = Book("tytuł1", "autor1", 123)
    let book2 = Book("tytuł2", "autor2", 231)    
    let book3 = Book("tytuł3", "autor3", 312)
    let book4 = Book("tytuł4", "autor4", 321)
    library.AddBook(book1)
    library.AddBook(book2)
    library.AddBook(book3)
    library.AddBook(book4)

    library.ListOfBooks()

    user.BorrowBook(book1)
    user.BorrowBook(book2)

    user.ListBorrowBooks()

    user.ReturnBook(book1)
    user.ListBorrowBooks()


main()