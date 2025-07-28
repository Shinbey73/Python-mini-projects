import random

def rock_paper_scissor():

    print("==========================Welcome to Rock-Paper-Scissor Game==========================")
    while True:
        print("Options: \n1. Rock\n2. Paper\n3. Scissor\n")

        try:
            user_choice = int(input("Enter your choice: "))
            if user_choice not in [1,2,3]:
                raise ValueError
            
        except ValueError:
            print("\nInvalid choice")
            continue
        
        choices = ["Rock", "Paper", "Scissor"]

        computer_choice = random.choice(choices)

        print(f"\nYour choice: {choices[user_choice - 1]}")
        print(f"Computer choice: {computer_choice}\n")

        user_choice = choices[user_choice - 1]

        winning_conditions = {
            "Rock": "Scissor",
            "Paper": "Rock",
            "Scissor": "Paper"
        }

        if user_choice == computer_choice:
            print("It's a tie")
        
        elif winning_conditions[user_choice] == computer_choice:
            print("You won")

        else:
            print("You lost")
        
        main_choice = input("Want to play again? (y/n)").lower()

        if main_choice == "y":
            continue
        else:
            print("\nThank you for playing")
            break
    
if __name__ == "__main__":
    rock_paper_scissor()