import random

def hangman_game():
    # 1. Setup predefined list of 5 words
    words = ["python", "developer", "intern", "django", "script"]
    
    # Select a random word
    secret_word = random.choice(words)
    word_length = len(secret_word)
    
    # Create the placeholder display (e.g., ['_', '_', '_', '_', '_', '_'])
    display_word = ["_"] * word_length
    
    # 2. Set variables
    attempts = 6
    guessed_letters = []
    
    print("=== Welcome to the Hangman Game ===")
    print(f"I have chosen a word with {word_length} letters.")
    print(" ".join(display_word))
    
    # 3. Main Game Loop
    while attempts > 0 and "_" in display_word:
        print(f"\nAttempts remaining: {attempts}")
        guess = input("Guess a letter: ").lower()

        # Input Validation: Ensure it's a single alphabet letter
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter.")
            continue
        
        # Check if already guessed
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try a different one.")
            continue
        
        # Add to history
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
            
            # Update the display list
            for index, char in enumerate(secret_word):
                if char == guess:
                    display_word[index] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong guess! '{guess}' is not in the word.")
            
        # Show current state of the word
        print("Current word: " + " ".join(display_word))
        print("-" * 30)

    # 4. Game Over Logic
    if "_" not in display_word:
        print("\n🎉 CONGRATULATIONS! You guessed the word:", secret_word)
    else:
        print("\n💀 GAME OVER! You ran out of attempts.")
        print(f"The word was: {secret_word}")

# Run the game
if __name__ == "__main__":
    hangman_game()