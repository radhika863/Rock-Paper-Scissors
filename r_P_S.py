import random

def rps():

    print("Welcome to the Game: Rock Paper Scissors!")

    user_input = input("Choose anyone of the following: Rock, Paper, Scissors: ").lower()
    comp = random.choice(["rock", "paper", "scissors"])

    print(f"You choose: {user_input.capitalize()}")
    print(f"We choose: {comp.capitalize()}")

    def game (user_input, comp):
        if user_input not in ["rock", "paper", "scissors"]:
            print("Invalid input! Please choose Rock, Paper, or Scissors.")
        elif (user_input == "rock" and comp == "scissors" ) or (user_input == "scissors" and comp == "paper") or (user_input == "paper" and comp == "rock"):
            return f"{user_input.upper()} BEATS {comp.upper()} \nWell, Congratulations, You Won!"
        elif user_input == comp:
            return "This game is a draw! PLAY AGAIN"
        else:
            return f"HAHAHAHA, {comp.upper()} BEATS {user_input.upper()} \nBetter luck next time!"
        
    print(game(user_input, comp))
    
    def play_again():
        pa = input("Want to play again: Y/N: ")
        if pa in ['Y' , 'y' , 'yes']:
            rps()
        elif pa in ["n", "N", "no"]:
            print("No worries, Your loss!")
        else:
            print("Areee, Enter a valid input, yes or no")
            play_again()
            
    play_again()

rps()

        

        
    