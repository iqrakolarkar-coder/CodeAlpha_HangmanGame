import random

def play_game():
    words = ["apple", "mango", "grape", "peach", "lemon"]
    secret_word = random.choice(words)

    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("\n🎮 Welcome to Hangman Game!")

    while wrong_guesses < max_wrong:
        # Display word
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word.strip())
        print("Guessed letters:", ", ".join(guessed_letters))
        print("Wrong guesses left:", max_wrong - wrong_guesses)

        # Check win condition
        if "_" not in display_word:
            print("🎉 Congratulations! You guessed the word:", secret_word)
            return

        guess = input("\nEnter a letter OR guess the full word: ").lower()

        # If user guesses full word
        if len(guess) > 1:
            if guess == secret_word:
                print("🎉 Amazing! You guessed the full word:", secret_word)
            else:
                print("❌ Wrong word guess!")
                wrong_guesses += 1
            continue

        # If user guesses letter
        if guess in guessed_letters:
            print("⚠ You already guessed that letter.")
        elif guess in secret_word:
            print("✅ Correct letter!")
            guessed_letters.append(guess)
        else:
            print("❌ Wrong letter!")
            guessed_letters.append(guess)
            wrong_guesses += 1

    print("\n💀 Game Over! The word was:", secret_word)


# Replay option
while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("👋 Thanks for playing!")
        break