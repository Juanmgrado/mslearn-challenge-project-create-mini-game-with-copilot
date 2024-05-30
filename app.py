import random

# write "Hello, World!" to the console
print("Hello, World!")

# lets try to create a simple game about sissors, paper, rock.
# rules: sissiors beats paper, paper beats rock, rock beats sissors.
# the player will play against the computer and will should to choose between sissors, paper, rock. if the player doesnt choose one
# of the three, a error massage appears and will ask to the player that choose a valid option.
# the points will be counted and the player that reach 3 points first will win the game.
# after every round, the player will be asked if he wants to play again. if the player choose "yes", the points will be keep and
# the game will continue. if the player choose "no", the game will end and the winner will be announced.
# the player (human or computer) that get 3 points first will win the game.
# show the players points and the computer points after every round.
#lest start the code: 

player_points = 0
computer_points = 0

function = ["sissors", "paper", "rock"]
player_choice = ""
computer_choice = ""
while True:
    # Player's turn
    player_choice = input("Choose sissors, paper, or rock: ")
    if player_choice not in function:
        print("Invalid choice. Please choose a valid option.")
        continue

    # Computer's turn
    computer_choice = random.choice(function)

    # Determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
        print(f"Player: {player_points} | Computer: {computer_points}")
    elif (player_choice == "sissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "rock" and computer_choice == "sissors"):
        print("Player wins this round!")
        print(f"Player: {player_points} | Computer: {computer_points}")
        player_points += 1
    else:
        print("Computer wins this round!")
        computer_points += 1
        print(f"Player: {player_points} | Computer: {computer_points}")

    # Check if any player has reached 3 points
    if player_points == 3:
        print("Player wins the game!")
        print(f"Player: {player_points} | Computer: {computer_points}")
        break
    elif computer_points == 3:
        print("Computer wins the game!")
        print(f"Player: {player_points} | Computer: {computer_points}")
        break

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "no":
        break
    elif play_again.lower() != "yes":
        print("Invalid choice. The game will continue.")

        