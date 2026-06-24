def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

# FIX: Refactored check_guess() from app.py into logic_utils.py with GitHub Copilot.
# Corrected reversed hint logic and verified using Streamlit and pytest.

def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # Preserve function signature; fix hint logic so messages match outcome.
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        # Guess is higher than secret -> tell player to go LOWER.
        return "Too High", "📉 Go LOWER!"
    else:
        # Guess is lower than secret -> tell player to go HIGHER.
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
