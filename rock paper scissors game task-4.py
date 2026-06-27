import random

def determine_winner(user_choice, computer_choice):
    """Evaluates choices and returns the round result string."""
    if user_choice == computer_choice:
        return "tie"
    
    # Win conditions for the human player
    winning_scenarios = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if winning_scenarios[user_choice] == computer_choice:
        return "user"
    return "computer"

def main():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    
    print("=== Rock, Paper, Scissors Game ===")
    print("Type 'exit' at any time to leave the game.\n")
    
    while True:
        # 1. Gather player selection with an exit condition
        user_input = input("Choose Rock, Paper, or Scissors: ").strip().lower()
        
        if user_input == "exit":
            break
        if user_input not in choices:
            print("Invalid selection. Choose 'rock', 'paper', or 'scissors'.\n")
            continue
            
        # 2. Generate random machine choice
        computer_input = random.choice(choices)
        print(f"Computer chose: {computer_input.capitalize()}")
        
        # 3. Calculate game logic and update score counters
        result = determine_winner(user_input, computer_input)
        
        if result == "tie":
            print("It's a tie match!")
        elif result == "user":
            print("You won this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
            
        # 4. Display continuous running scoreboard
        print(f"Current Score -> You: {user_score} | Computer: {computer_score}\n")
        print("-" * 30)

    print("\n=== Final Scoreboard ===")
    print(f"You: {user_score} | Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
