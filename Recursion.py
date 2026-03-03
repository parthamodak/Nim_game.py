def open_doll(size):
    print("Opening the doll =", size)      # (1)

    if size == 0:                                    # (2)
        print("Base case reached")                   # (3)
        return                                      # (4)

    print("Opening doll", size)                     # (5)

    open_doll(size - 1)                             # (6)

    print("Closing doll", size)                     # (7)



size = int(input("Enter the number of dolls: "))
open_doll(size)                                          # (8)