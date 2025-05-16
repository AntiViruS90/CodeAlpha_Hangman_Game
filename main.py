from random import choice

WORDS = [
    "PYTHON",
    "PROGRAMMING",
    "SOFTWARE",
    "COMPUTER",
    "DATABASE",
    "ALGORITHM",
    "NETWORK"
]

HANGMAN_ART = [
    """
      ------
      |    |
           |
           |
           |
           |
    ==========""",
    """
      ------
      |    |
      O    |
           |
           |
           |
    ==========""",
    """
      ------
      |    |
      O    |
      |    |
           |
           |
    ==========""",
    """
      ------
      |    |
      O    |
     /|    |
           |
           |
    ==========""",
    """
      ------
      |    |
      O    |
     /|\\   |
           |
           |
    ==========""",
    """
      ------
      |    |
      O    |
     /|\\   |
     /     |
           |
    ==========""",
    """
      ------
      |    |
      O    |
     /|\\   |
     / \\   |
           |
    =========="""
]


def play_hangman():
    word = choice(WORDS)
    word_letters = set(word)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    display_word = ["_" if letter.isalpha() else letter for letter in word]

    print("Welcome to Hangman!")
    print(HANGMAN_ART[incorrect_guesses])
    print("Word: ", " ".join(display_word))

    while incorrect_guesses < max_incorrect and set(display_word) != set(word):
        guess = input("Guess a letter: ").upper()

        if len(guess) < 1 or not guess.isalpha():
            print(f"Please enter a single letter. {guess}")
            continue
        if guess in guessed_letters:
            print("You're already guessed this letter")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            for i, letter in enumerate(word):
                if letter == guess:
                    display_word[i] = guess
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print("Incorrect guess!")

        print(HANGMAN_ART[incorrect_guesses])
        print("Word: ", " ".join(display_word))
        print("Guessed letters: ", ", ".join(sorted(guessed_letters)))

    if set(display_word) == set(word):
        print("Congratulations! You guessed the word: ", word)
    else:
        print("Game over! The word was: ", word)


if __name__ == "__main__":
    while True:
        play_hangman()

        play_again = input("Do you want to play again? (Y/N): ").strip().upper()
        if play_again != "Y":
            print("Thanks for playing!")
            break
