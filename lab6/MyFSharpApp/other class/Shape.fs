[<AbstractClass>]
type Shape() =
    abstract member Area: unit -> float

    member this.View() =
        printfn "To jest kształt"

type Circle(radius: float) =
    inherit Shape()

    override this.Area() =
        System.Math.PI * radius * radius

type IShape =

    abstract member Area: float
    abstract member Area1: unit -> float

type Circle1(radius: float) =
    interface IShape with
    // properties
        member this.Area = System.Math.PI * radius * radius

    // methods
    member this.Area1(): float =
        System.Math.PI * radius * radius
        