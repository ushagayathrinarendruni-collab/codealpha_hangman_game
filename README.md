# codealpha_hangman_game
🐍 CodeAlpha Hangman Game

A professional console-based Hangman Game developed in Python as part of the CodeAlpha Python Programming Internship.

The player must guess a randomly selected hidden word one letter at a time while avoiding six incorrect guesses. The game includes hints, input validation, score calculation, game statistics, and replay functionality.

---

🎯 Project Objective

The objective of this project is to demonstrate fundamental Python programming concepts by building an interactive text-based Hangman game.

CodeAlpha Task

Task 1: Hangman Game

«Create a simple text-based Hangman game where the player guesses a word one letter at a time.»

---

✨ Features

- 🎲 Random word selection
- 🔤 One-letter-at-a-time guessing
- 💡 Word hints
- ❤️ Six maximum wrong guesses
- 🛡️ Input validation
- 🔄 Duplicate-guess prevention
- 🎨 ASCII Hangman graphics
- 🏆 Win detection
- 💀 Game-over detection
- ⭐ Score calculation
- 📊 Game statistics
- 🔁 Replay option
- 📈 Win-rate calculation
- 🐍 Built using standard Python

---

🛠️ Technologies Used

Technology| Purpose
Python| Core programming language
"random"| Random word selection
Lists| Store guessed letters
Dictionary| Store words and hints
Functions| Organize program logic
Loops| Control game flow
Conditional Statements| Validate guesses and game states
Strings| Process words and user input

---

📂 Project Structure

CodeAlpha_Hangman_Game/
│
├── hangman.py
└── README.md

"hangman.py"

Contains the complete Hangman game implementation, including:

- Word selection
- Hangman display
- Input validation
- Guess processing
- Score calculation
- Game statistics
- Replay functionality

---

⚙️ Requirements

You only need:

- Python 3.x
- A terminal or command prompt
- VS Code or any Python-compatible editor

No external Python packages are required.

---

🚀 How to Run

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

2. Open the project folder

cd CodeAlpha_Hangman_Game

3. Run the program

python hangman.py

If your system uses "python3":

python3 hangman.py

---

🎮 How to Play

1. Start the program.
2. A random word is selected.
3. Read the displayed hint.
4. Enter one alphabet letter.
5. Correct guesses reveal the letter.
6. Incorrect guesses reduce your remaining lives.
7. Guess the complete word before six incorrect guesses to win.
8. After the game, choose whether to play again.

---

🖥️ Sample Gameplay

============================================================
             🐍 CODEALPHA HANGMAN
============================================================

🎯 Guess the hidden word one letter at a time!
💡 Use the hint to help you.
❤️  You have 6 wrong guesses per game!

============================================================
                    🎮 NEW GAME
============================================================

💡 Hint: A popular programming language
🔤 Word Length: 6 letters
❤️  Maximum Wrong Guesses: 6

------------------------------------------------------------

           +---+
           |   |
               |
               |
               |
               |
        =========

🔤 Word: _ _ _ _ _ _
❤️  Lives Remaining: 6

👉 Enter a letter: p

✅ Excellent! 'P' is correct.

🔤 Word: P _ _ _ _ _

---

🧠 Concepts Demonstrated

This project demonstrates the following Python concepts:

- Variables
- Strings
- Lists
- Dictionaries
- Functions
- "while" loops
- "if-elif-else"
- "for" loops
- User input
- Input validation
- Random selection
- Boolean logic
- Arithmetic operations
- Function return values

---

📊 Scoring System

The score is calculated using the length of the word and the number of incorrect guesses.

Base Score = Word Length × 100

Penalty = Wrong Guesses × 25

Final Score = Base Score − Penalty

The minimum score is always "0".

---

🔒 Input Validation

The game checks user input to prevent invalid guesses.

The program rejects:

- Numbers
- Symbols
- Multiple characters
- Previously guessed letters

Example:

👉 Enter a letter: abc

⚠️ Please enter exactly one letter.

---

🔮 Future Improvements

Possible future enhancements include:

- 🎚️ Easy, Medium and Hard difficulty levels
- 📚 Larger word database
- 🏅 High-score leaderboard
- 💾 Save scores to a file
- 🎨 Colored terminal interface
- 🔊 Sound effects
- 🖼️ GUI version using Tkinter
- 🌐 Web-based version
- 👥 Two-player mode

---

🎓 Internship

This project was developed as part of the:

CodeAlpha Python Programming Internship

Task: Hangman Game

---

👩‍💻 Author

Usha Gayathri

Python Programming Intern

---

📌 Project Status

Status: ✅ Completed

Version: 1.0

---

⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

📜 License

This project is created for educational and internship purposes.
