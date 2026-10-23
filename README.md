# CodeAlpha Basic Chatbot

CodeAlpha Python Programming internship task, by Steven Rios.

## Overview
A rule-based console chatbot (CodeBot) built with functions and `if/elif`. It answers hello, how are you, what is your name, what time is it, help and thanks, ignores case and punctuation, gives a fallback reply for anything else, and keeps chatting until you say bye.

## How to run
Requires Python 3.8+.
```bash
python chatbot.py
```
Run the tests:
```bash
python -m unittest -v
```

## Sample output
Captured from a scripted run with piped input (typed answers are not echoed when piped).
```text
CodeBot: Hello! I'm CodeBot. Type 'bye' to exit.
You: CodeBot: Hi! How can I help you today?
You: CodeBot: I'm fine, thanks! How about you?
You: CodeBot: I'm CodeBot, a simple rule-based chatbot.
You: CodeBot: You can say: hello, how are you, what is your name, what time is it, help, or bye.
You: CodeBot: Sorry, I don't understand that yet. Type 'help' to see what I know.
You: CodeBot: Goodbye! Have a great day.
```

## Concepts used
- `if/elif/else` rules
- Functions
- `while` loop with input/output
- String cleanup (`lower`, `str.translate`)
- `datetime` for the time reply
- `unittest` with mocked input

## LinkedIn demo script (60-90 s)
1. (0-10s) Intro: "CodeAlpha Task 4: a basic rule-based chatbot."
2. (10-30s) Show `get_response` in `chatbot.py` and its if-elif rules.
3. (30-65s) Run it: `Hello!`, `HOW ARE YOU?`, `what's your name`, `what time is it`, a random sentence (fallback), then `bye`.
4. (65-85s) Run the tests and thank @CodeAlpha.

## License
MIT, see [LICENSE](LICENSE).
