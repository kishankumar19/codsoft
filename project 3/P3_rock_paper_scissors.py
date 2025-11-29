import random
import os

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        
    def clear_screen(self):
        """Clear the terminal screen for better readability"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_welcome(self):
        """Display welcome message and game rules"""
        print("🎮" + "="*50 + "🎮")
        print("           WELCOME TO ROCK PAPER SCISSORS!")
        print("🎮" + "="*50 + "🎮")
        print("\n📖 GAME RULES:")
        print("  • Rock beats Scissors ✊ beats ✌️")
        print("  • Scissors beats Paper ✌️ beats ✋")
        print("  • Paper beats Rock ✋ beats ✊")
        print("  • Same choice means tie!")
        print("\n" + "="*55)
    
    def get_user_choice(self):
        """Get and validate user's choice"""
        while True:
            print("\nChoose your weapon:")
            print("1. Rock ✊")
            print("2. Paper ✋")
            print("3. Scissors ✌️")
            
            choice = input("\nEnter your choice (1/2/3 or rock/paper/scissors): ").lower().strip()
            
            # Handle numeric input
            if choice in ['1', 'rock']:
                return 'rock'
            elif choice in ['2', 'paper']:
                return 'paper'
            elif choice in ['3', 'scissors']:
                return 'scissors'
            else:
                print("❌ Invalid choice! Please enter 1, 2, 3 or rock, paper, scissors.")
    
    def get_computer_choice(self):
        """Generate computer's random choice"""
        return random.choice(self.choices)
    
    def determine_winner(self, user_choice, computer_choice):
        """Determine the winner of the round"""
        if user_choice == computer_choice:
            return 'tie'
        
        winning_combinations = {
            'rock': 'scissors',      # Rock beats scissors
            'scissors': 'paper',     # Scissors beat paper
            'paper': 'rock'          # Paper beats rock
        }
        
        if winning_combinations[user_choice] == computer_choice:
            return 'user'
        else:
            return 'computer'
    
    def display_choices(self, user_choice, computer_choice):
        """Display both choices with emojis"""
        choice_emojis = {
            'rock': '✊',
            'paper': '✋',
            'scissors': '✌️'
        }
        
        print(f"\n{" YOUR CHOICE ":=^50}")
        print(f"     {user_choice.upper()} {choice_emojis[user_choice]}")
        print(f"\n{" COMPUTER'S CHOICE ":=^50}")
        print(f"     {computer_choice.upper()} {choice_emojis[computer_choice]}")
    
    def display_result(self, result, user_choice, computer_choice):
        """Display the result of the round"""
        print(f"\n{" RESULT ":=^50}")
        
        if result == 'tie':
            print("🤝 IT'S A TIE! 🤝")
            print(f"Both chose {user_choice}")
        elif result == 'user':
            print("🎉 YOU WIN! 🎉")
            self.user_score += 1
            # Show why user won
            if user_choice == 'rock':
                print("✊ Rock crushes Scissors! ✌️")
            elif user_choice == 'paper':
                print("✋ Paper covers Rock! ✊")
            else:
                print("✌️ Scissors cut Paper! ✋")
        else:
            print("💻 COMPUTER WINS! 💻")
            self.computer_score += 1
            # Show why computer won
            if computer_choice == 'rock':
                print("✊ Rock crushes Scissors! ✌️")
            elif computer_choice == 'paper':
                print("✋ Paper covers Rock! ✊")
            else:
                print("✌️ Scissors cut Paper! ✋")
        
        self.rounds_played += 1
    
    def display_score(self):
        """Display current score"""
        print(f"\n{" SCOREBOARD ":=^50}")
        print(f"👤 You: {self.user_score}  |  💻 Computer: {self.computer_score}  |  🔢 Rounds: {self.rounds_played}")
        
        if self.rounds_played > 0:
            win_percentage = (self.user_score / self.rounds_played) * 100
            print(f"📊 Your win rate: {win_percentage:.1f}%")
    
    def play_round(self):
        """Play one round of the game"""
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        
        self.clear_screen()
        self.display_choices(user_choice, computer_choice)
        
        result = self.determine_winner(user_choice, computer_choice)
        self.display_result(result, user_choice, computer_choice)
        self.display_score()
    
    def ask_play_again(self):
        """Ask user if they want to play another round"""
        while True:
            play_again = input("\n🔄 Would you like to play again? (y/n): ").lower().strip()
            if play_again in ['y', 'yes', '1']:
                return True
            elif play_again in ['n', 'no', '0']:
                return False
            else:
                print("❌ Please enter 'y' for yes or 'n' for no.")
    
    def display_final_results(self):
        """Display final results when game ends"""
        print(f"\n{" FINAL RESULTS ":=^50}")
        self.display_score()
        
        if self.user_score > self.computer_score:
            print("🎊 CONGRATULATIONS! YOU WON THE GAME! 🎊")
        elif self.user_score < self.computer_score:
            print("🤖 Better luck next time! The computer won the game.")
        else:
            print("🤝 The game ended in a tie! Well played!")
        
        print("\nThanks for playing! 👋")
        print("="*55)
    
    def reset_game(self):
        """Reset the game for a fresh start"""
        self.user_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.clear_screen()
        self.display_welcome()

def main():
    """Main function to run the game"""
    game = RockPaperScissors()
    
    try:
        game.clear_screen()
        game.display_welcome()
        
        while True:
            game.play_round()
            
            if not game.ask_play_again():
                game.display_final_results()
                break
            else:
                game.clear_screen()
                game.display_welcome()
                
    except KeyboardInterrupt:
        print(f"\n\nGame interrupted. Final score: You {game.user_score} - {game.computer_score} Computer")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()