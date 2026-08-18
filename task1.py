import random


# ============================================================
# CODEALPHA PYTHON INTERNSHIP
# TASK 1: HANGMAN GAME
# ============================================================

# Predefined words with hints
WORDS = {
    "python": "A popular programming language",
    "computer": "An electronic machine used to process data",
    "algorithm": "A step-by-step procedure to solve a problem",
    "database": "A structured collection of information",
    "developer": "A person who creates software",
    "internet": "A worldwide network of computers",
    "software": "Programs that run on a computer",
    "keyboard": "An input device used for typing",
    "technology": "Application of scientific knowledge",
    "programming": "Writing instructions for a computer"
}

MAX_WRONG_GUESSES = 6


# ============================================================
# HANGMAN DRAWINGS
# ============================================================

def display_hangman(wrong_guesses):
    """Display the Hangman figure."""

    stages = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,

        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,

        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,

        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,

        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,

        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,

        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]

    print(stages[wrong_guesses])


# ============================================================
# DISPLAY WORD
# ============================================================

def display_word(word, guessed_letters):
    """Return the word with unguessed letters hidden."""

    result = []

    for letter in word:
        if letter in guessed_letters:
            result.append(letter.upper())
        else:
            result.append("_")

    return " ".join(result)


# ============================================================
# CHECK WIN
# ============================================================

def has_won(word, guessed_letters):
    """Check whether every letter has been guessed."""

    return all(letter in guessed_letters for letter in word)


# ============================================================
# GET VALID GUESS
# ============================================================

def get_guess(guessed_letters):
    """Get and validate a letter from the player."""

    while True:

        guess = input("\n👉 Enter a letter: ").strip().lower()

        if len(guess) != 1:
            print("⚠️ Please enter exactly one letter.")
            continue

        if not guess.isalpha():
            print("⚠️ Please enter an alphabet letter.")
            continue

        if guess in guessed_letters:
            print("🔄 You already guessed that letter.")
            continue

        return guess


# ============================================================
# CALCULATE SCORE
# ============================================================

def calculate_score(word, wrong_guesses):
    """Calculate score based on word length and mistakes."""

    base_score = len(word) * 100
    penalty = wrong_guesses * 25

    score = max(base_score - penalty, 0)

    return score


# ============================================================
# PLAY ONE GAME
# ============================================================

def play_game():
    """Run one complete Hangman game."""

    word = random.choice(list(WORDS.keys()))
    hint = WORDS[word]

    guessed_letters = []
    wrong_guesses = 0

    print("\n" + "=" * 60)
    print("                    🎮 NEW GAME")
    print("=" * 60)

    print(f"\n💡 Hint: {hint}")
    print(f"🔤 Word Length: {len(word)} letters")
    print(f"❤️  Maximum Wrong Guesses: {MAX_WRONG_GUESSES}")

    while wrong_guesses < MAX_WRONG_GUESSES:

        print("\n" + "-" * 60)

        display_hangman(wrong_guesses)

        print(f"🔤 Word: {display_word(word, guessed_letters)}")

        if guessed_letters:
            print(
                "📝 Guessed:",
                ", ".join(sorted(guessed_letters)).upper()
            )

        remaining_lives = MAX_WRONG_GUESSES - wrong_guesses

        print(f"❤️  Lives Remaining: {remaining_lives}")

        # Check win
        if has_won(word, guessed_letters):

            score = calculate_score(word, wrong_guesses)

            print("\n" + "=" * 60)
            print("                🎉 YOU WON! 🎉")
            print("=" * 60)

            print(f"🏆 Word: {word.upper()}")
            print(f"⭐ Score: {score}")

            return True, score

        # Get valid input
        guess = get_guess(guessed_letters)

        guessed_letters.append(guess)

        # Correct guess
        if guess in word:

            print(f"✅ Excellent! '{guess.upper()}' is correct.")

        # Wrong guess
        else:

            wrong_guesses += 1

            print(
                f"❌ Sorry! '{guess.upper()}' "
                f"is not in the word."
            )

    # ========================================================
    # GAME OVER
    # ========================================================

    display_hangman(wrong_guesses)

    print("\n" + "=" * 60)
    print("                 💀 GAME OVER")
    print("=" * 60)

    print(f"🔤 The correct word was: {word.upper()}")
    print("⭐ Score: 0")

    return False, 0


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    games_played = 0
    wins = 0
    total_score = 0

    print("\n" + "=" * 60)
    print("             🐍 CODEALPHA HANGMAN")
    print("=" * 60)

    print("\n🎯 Guess the hidden word one letter at a time!")
    print("💡 Use the hint to help you.")
    print("❤️  You have 6 wrong guesses per game.")

    while True:

        won, score = play_game()

        games_played += 1

        if won:
            wins += 1
            total_score += score

        losses = games_played - wins

        print("\n" + "-" * 60)
        print("                    📊 STATISTICS")
        print("-" * 60)

        print(f"🎮 Games Played : {games_played}")
        print(f"🏆 Wins         : {wins}")
        print(f"💀 Losses       : {losses}")
        print(f"⭐ Total Score  : {total_score}")

        replay = input(
            "\n🔄 Play again? (y/n): "
        ).strip().lower()

        if replay != "y":
            break

    # ========================================================
    # FINAL RESULTS
    # ========================================================

    print("\n" + "=" * 60)
    print("                  👋 THANK YOU!")
    print("=" * 60)

    print(f"🎮 Games Played : {games_played}")
    print(f"🏆 Wins         : {wins}")
    print(f"💀 Losses       : {games_played - wins}")
    print(f"⭐ Total Score  : {total_score}")

    if games_played > 0:

        win_percentage = (wins / games_played) * 100

        print(
            f"📈 Win Rate     : {win_percentage:.1f}%"
        )

    print("\n🚀 Keep learning Python!")
    print("=" * 60)


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()