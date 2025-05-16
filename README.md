# CodeAlpha_Hangman_Game

## Overview

Hangman is a console-based word guessing game written in Python. The player has **6 attempts** to guess a randomly selected word by suggesting one letter at a time. Correct guesses reveal the letter's positions in the word, while incorrect guesses advance the hangman drawing. The game ends when the word is fully guessed or all attempts are exhausted.

## Features

- Random word selection from a predefined list
- 6 attempts to guess the word
- ASCII art displaying the hangman’s progress
- Option to play again after each game
- Input validation for single letters and repeated guesses

## Requirements

- **Programming Language**: Python 3.x

## Installation

1. Clone or download the repository to your local machine.
2. Ensure Python 3 is installed. You can download it from [python.org](https://www.python.org/downloads/).

## Running the Game

The executable file is `main.py`. Run the game using the following commands based on your operating system:

### Unix/Linux Systems
```bash
python3 main.py
```

### Windows (Microsoft)
```bash
python main.py
```

## How to Play

1. Launch the game using the appropriate command above.
2. The game displays a series of underscores representing each letter in the hidden word.
3. Enter one letter at a time to guess the word.
4. Correct guesses fill in the corresponding blanks, while incorrect guesses update the hangman drawing.
5. You have 6 incorrect guesses before the game ends.
6. After the game ends (win or lose), choose to play again by entering `Y` (yes) or `N` (no).

## Example Gameplay

```
Welcome to Hangman!
      ------
      |    |
           |
           |
           |
           |
    ==========
Word:  _ _ _ _ _ _
Guess a letter: a
Good guess!
      ------
      |    |
           |
           |
           |
           |
    ==========
Word:  _ A _ _ _ _
Guessed letters: A
```

## Video Gameplay

[![asciicast](https://asciinema.org/a/PHznnPLFc0W9D9hD55hw5ja3j.svg)](https://asciinema.org/a/PHznnPLFc0W9D9hD55hw5ja3j)