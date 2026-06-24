# 💭 Reflection: Game Glitch Investigator

##QUESTION
Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.
---

## 1. What was broken when you started?

When I first launched the Streamlit application, the game loaded successfully and allowed me to begin guessing numbers. As I played several rounds, I noticed that the game contained multiple logic errors that affected the gameplay. Instead of modifying the code immediately, I observed the behavior carefully and documented each issue so that it could be reproduced later.

The first bug I noticed was that the hint messages were reversed. When the secret number was **40**, guessing **50** and **75** displayed **"Go HIGHER!"** even though the correct hint should have been **"Go LOWER!"** Likewise, when I guessed **25**, the game displayed **"Go LOWER!"** instead of **"Go HIGHER!"**

The second issue was that The secret number was converted to a string on even-numbered attempts, causing incorrect comparisons and requiring a fallback to string comparison.

The third issue was that the game converted the secret number to a string on even-numbered attempts, causing inconsistent comparisons and triggering the TypeError fallback.
---
## Document at least 3 bugs you found. Add rows as needed.
**Bug Reproduction Log**


| Input                   | Expected Behavior    |Actual Behavior    |Console Output / Error|
| ----------------------- | -------------------- | ---------------------- | -----------------
| Secret = 40, Guess = 50 | Display "Go LOWER!"  | Displayed "Go HIGHER!" | None|
| Secret = 40, Guess = 75 | Display "Go LOWER!"  | Displayed "Go HIGHER!" | None|
| Secret = 40, Guess = 25 | Display "Go HIGHER!" | Displayed "Go LOWER!"  | None|
---

### AI Investigation

I used GitHub Copilot Chat to investigate the reversed hint bug. I attached `app.py` and `logic_utils.py` and asked the AI to explain the logic without fixing the code. The AI explained that the `check_guess()` function correctly determines whether a guess is too high or too low, but the messages associated with those outcomes are reversed. It also pointed out that the game sometimes converts the secret number to a string, causing string comparisons instead of numeric comparisons on some attempts. This explanation helped me understand the bug before making any code changes.


## Describe one specific glitch you found and ask the AI to explain the underlying logic causing it.

One specific glitch I found was that the hint messages were reversed. When the secret number was **40**, guesses of **50** and **75** displayed **"Go HIGHER!"** instead of **"Go LOWER!"**, while a guess of **25** displayed **"Go LOWER!"** instead of **"Go HIGHER!"**.

I asked GitHub Copilot Chat to explain the logic behind this behavior without fixing the code. The AI explained that the game first compares the player's guess with the secret number in the `check_guess()` function. When the guess is greater than the secret number, the function correctly identifies the result as **"Too High"**, but it incorrectly associates that result with the message **"Go HIGHER!"** instead of **"Go LOWER!"**. Likewise, when the guess is lower than the secret number, it returns **"Too Low"** but displays **"Go LOWER!"** instead of **"Go HIGHER!"**.

The AI also pointed out that on even-numbered attempts, the secret number is converted to a string, causing the program to fall back to string (lexicographic) comparison after a `TypeError`. This could produce additional incorrect behavior for certain guesses. The explanation helped me understand the underlying logic before making any code changes.

---

## 2. How did you use AI as a teammate?

I used **GitHub Copilot Chat** and **ChatGPT** as AI teammates during this project. GitHub Copilot Chat helped me inspect the code, refactor `check_guess()` from `app.py` into `logic_utils.py`, fix the reversed hint logic, remove the string-conversion bug, and generate pytest tests. I used ChatGPT to help me interpret the project instructions, review Copilot's proposed changes, and decide whether the fixes matched the assignment requirements.

One correct AI suggestion was Copilot's recommendation to move `check_guess()` into `logic_utils.py` and fix the reversed hint messages. Copilot changed the logic so that a guess greater than the secret returns **"Too High"** with **"Go LOWER!"**, while a guess less than the secret returns **"Too Low"** with **"Go HIGHER!"**. I verified this by running the Streamlit app and testing guesses against the visible secret number in Developer Debug Info. For example, when the secret was **70**, guesses of **90** and **85** correctly showed **"Go LOWER!"**, and a guess of **65** correctly showed **"Go HIGHER!"**.

One misleading AI-related issue occurred during testing. The original starter tests still expected `check_guess()` to return only a string such as `"Win"` or `"Too High"`, but the refactored function returned a tuple like `("Too High", "Go LOWER!")`. When I ran `python -m pytest`, three starter tests failed. This showed me that even after AI-generated fixes, I still needed to review and update the tests so they matched the actual function behavior.

---

## 3. Debugging and testing your fixes

I decided that the first bug was fixed only after I manually verified the game's behavior instead of relying solely on the AI's suggestion. After accepting the refactored code, I restarted the Streamlit application and tested several guesses against the secret number displayed in the Developer Debug Info panel. The hint messages matched the expected behavior, confirming that the first bug had been repaired.

One manual test I performed used a secret number of **70**. I guessed **90** and **85**, and the game correctly displayed **"Go LOWER!"**. I then guessed **65**, and the game correctly displayed **"Go HIGHER!"**. These results showed that the reversed hint logic had been corrected.

GitHub Copilot also helped me design regression tests for the repaired check_guess() function. After updating the original starter tests to match the new tuple return values, I ran python -m pytest, and all six tests passed. This confirmed that both the manual testing and the automated tests verified the correctness of my repairs.

---

## 4. What did you learn about Streamlit and state?
**  How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Before this project, I did not fully understand how Streamlit reruns a program after every user interaction. I learned that every time a user clicks a button or enters new input, Streamlit reruns the entire script from top to bottom. The `st.session_state` object stores important values such as the secret number, score, attempts, and game status so they are not reset during each rerun. Without session state, the game would lose its progress every time the app refreshed, making it impossible to play correctly.

---

## 5. Looking ahead: your developer habits

One habit I want to continue using is verifying every AI-generated suggestion before accepting it. During this project, I carefully reviewed each GitHub Copilot code change, tested the game manually, and used pytest to confirm the fixes worked correctly. This process helped me discover that the original starter tests no longer matched the updated function behavior.

Next time I work with AI on a coding task, I will ask the AI to explain its proposed changes before applying them and will run automated tests earlier in the debugging process instead of waiting until after several fixes have been made.

This project changed the way I think about AI-generated code by showing me that AI is a helpful programming assistant but not a replacement for careful human judgment. I learned that every AI-generated solution should be reviewed, tested, and verified before it is accepted into a project.

---

