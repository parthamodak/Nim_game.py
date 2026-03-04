def open_doll(size):
    print("Total Opening the doll =", size)

    if size == 1:
        print("Base case reached")
        print("closing doll", size)
        return

    print("Opening doll", size)

    open_doll(size - 1)

    print("Closing doll", size)


size = int(input("Enter the number of dolls: "))
open_doll(size)