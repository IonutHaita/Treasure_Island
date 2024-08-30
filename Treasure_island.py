print("Welcome to Treasure island!")
print("Your mission is to find the treasure")

invalid = False
good_dir_choice = False
good_choice = False

direction = input("You're at a cross road. Which path do you want to take? Left or Right\n")
if direction != "Left" and direction != "Right":
    print("Invalid input! Try again!")
    invalid = True
good_dir_choice = True if direction == "Left" else False

if good_dir_choice:
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice = input("Type Wait to wait for a boat or Swim to try and swim across.\n")
    if choice != "Wait" and choice != "Swim":
        print("Invalid input! Try again!")
        invalid = True
    good_choice = True if choice == "Wait" else False
if not good_dir_choice and not invalid:
    print("You lost! Try again!")
          
if good_dir_choice and not good_choice and not invalid:
    print("You lost! Try again!")
if good_dir_choice and good_choice:
    print("You arrive on the island unharmed. There is a house with three doors.")
    last_choice = input("One red, one yellow and one blue. Which colour do you choose? Type Red, Yellow or Blue\n")
    if last_choice != "Red" and last_choice != "Yellow" and last_choice != "Blue":
        print("Invalid input! Try again!")
        invalid = True
    if last_choice == "Yellow":
        print("Congratulations, you are saved!")
    elif not invalid and last_choice != "Yellow":
        print("You lost! Try again!")

