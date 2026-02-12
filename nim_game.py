try:
    num_of_stones = int(input("Enter the number of stones in the pile: "))
    print("There are", num_of_stones, "stones in the pile.")
except ValueError:
    print("Invalid input. Please enter a valid number of stones.")

while num_of_stones > 0:
    print("\nYour turn.")
    print("Stones left:", num_of_stones)
    take = int(input("you can take 1, 2, or 3 stones: "))
    if take not in [1, 2, 3] or take > num_of_stones:
        print("Invalid move. Try again.")
        continue
    num_of_stones -= take

    if num_of_stones == 0:
        print("there is not stone left. you win!")
        break
    comp_take = num_of_stones  % 4
    if comp_take == 0:
        comp_take = 1
    print("\nComputer takes:", comp_take)
    num_of_stones -= comp_take

    if num_of_stones == 0:
        print("Computer took the last stone. Computer wins!")
        break

    