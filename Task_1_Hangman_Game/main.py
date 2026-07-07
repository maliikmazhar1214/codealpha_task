import random

def play_hangman():
    # Step 1: Word list & random pick
    words = ["python", "hangman", "keyboard", "monitor", "science"]
    secret_word = random.choice(words)

    # Step 2: Setup
    display = ["_"] * len(secret_word)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("🎮 Welcome to Hangman!")
    print(f"Hint: The word has {len(secret_word)} letters\n")

    # Step 3: Game loop
    while wrong_guesses < max_wrong and "_" in display:
        print(f"Word:    {' '.join(display)}")
        print(f"Wrong:   {wrong_guesses}/{max_wrong}")
        print(f"Guessed: {', '.join(guessed_letters) or 'None'}")

        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Enter one letter only!\n")
            continue
        if guess in guessed_letters:
            print("⚠️  Already guessed that!\n")
            continue

        guessed_letters.append(guess)

        # Check guess
        if guess in secret_word:
            print("✅ Good guess!\n")
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    display[i] = guess
        else:
            wrong_guesses += 1
            print(f"❌ Wrong! {max_wrong - wrong_guesses} chances left\n")

    # Step 4: Result
    if "_" not in display:
        print(f"🎉 YOU WIN! Word: {secret_word}")
    else:
        print(f"💀 GAME OVER! Word was: {secret_word}")

# Run it
play_hangman()
