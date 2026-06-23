# 💭 Reflection: Game Glitch Investigator

##QUESTION
Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |

# 💭 ANSWER

## 1. What was broken when you started?

When I first launched the Streamlit application, the game loaded successfully and allowed me to begin guessing numbers. As I played several rounds, I noticed that the game contained multiple logic errors that affected the gameplay. Instead of modifying the code immediately, I observed the behavior carefully and documented each issue so that it could be reproduced later.

The first bug I noticed was that the hint messages were reversed. When the secret number was **40**, guessing **50** and **75** displayed **"Go HIGHER!"** even though the correct hint should have been **"Go LOWER!"** Likewise, when I guessed **25**, the game displayed **"Go LOWER!"** instead of **"Go HIGHER!"**

The second issue was that the number of attempts displayed on the main game screen did not match the value shown in the **Developer Debug Info** panel. This made it difficult to determine the actual game state.

The third issue was that the **Developer Debug Info** exposed the secret number to the player. Since the secret value was visible during gameplay, the game could easily be won without actually guessing, defeating the purpose of the game.

---
### Bug Reproduction Log

| Input                   | Expected Behavior    |Actual Behavior    |Console Output / Error|
| ----------------------- | -------------------- | ---------------------- | -----------------
| Secret = 40, Guess = 50 | Display "Go LOWER!"  | Displayed "Go HIGHER!" | None|
| Secret = 40, Guess = 75 | Display "Go LOWER!"  | Displayed "Go HIGHER!" | None|
| Secret = 40, Guess = 25 | Display "Go HIGHER!" | Displayed "Go LOWER!"  | None|
---

---

### AI Investigation

I used GitHub Copilot Chat to investigate the reversed hint bug. I attached `app.py` and `logic_utils.py` and asked the AI to explain the logic without fixing the code. The AI explained that the `check_guess()` function correctly determines whether a guess is too high or too low, but the messages associated with those outcomes are reversed. It also pointed out that the game sometimes converts the secret number to a string, causing string comparisons instead of numeric comparisons on some attempts. This explanation helped me understand the bug before making any code changes.


## QUESTION
Describe one specific glitch you found and ask the AI to explain the underlying logic causing it.

## ANSWER
### AI Explanation of a Specific Glitch

One specific glitch I found was that the hint messages were reversed. When the secret number was **40**, guesses of **50** and **75** displayed **"Go HIGHER!"** instead of **"Go LOWER!"**, while a guess of **25** displayed **"Go LOWER!"** instead of **"Go HIGHER!"**.

I asked GitHub Copilot Chat to explain the logic behind this behavior without fixing the code. The AI explained that the game first compares the player's guess with the secret number in the `check_guess()` function. When the guess is greater than the secret number, the function correctly identifies the result as **"Too High"**, but it incorrectly associates that result with the message **"Go HIGHER!"** instead of **"Go LOWER!"**. Likewise, when the guess is lower than the secret number, it returns **"Too Low"** but displays **"Go LOWER!"** instead of **"Go HIGHER!"**.

The AI also pointed out that on even-numbered attempts, the secret number is converted to a string, causing the program to fall back to string (lexicographic) comparison after a `TypeError`. This could produce additional incorrect behavior for certain guesses. The explanation helped me understand the underlying logic before making any code changes.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
