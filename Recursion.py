def open_doll(size):
    print("Opening the doll =", size)      # (1)

    if size == 0:                                    # (2)
        print("Base case reached")                   # (3)
        return                                      # (4)

    print("Opening doll", size)                     # (5)

    open_doll(size - 1)                             # (6)

    print("Closing doll", size)                     



size = int(input("Enter the number of dolls: "))
open_doll(size)                                          

# here is a thing when this code exicute it allocate the same amount of
#  the memory what it need to open then it for the loasing time it require same like open is 10 so ending will be 10 total 20 memory allocated