"""Basic rule-based chatbot (CodeAlpha Python Task 4)."""
import string
from datetime import datetime

BOT_NAME = "CodeBot"


def clean(text):
    """Lowercase the text and remove punctuation so 'Hello!!' == 'hello'."""
    return text.lower().translate(str.maketrans("", "", string.punctuation)).strip()


def help_text():
    return "You can say: hello, how are you, what is your name, what time is it, help, or bye."


def get_response(message):
    """Return the bot's reply for one user message using simple if-elif rules."""
    text = clean(message)
    if text in ("hello", "hi", "hey"):
        return "Hi! How can I help you today?"
    elif text in ("how are you", "how are you doing"):
        return "I'm fine, thanks! How about you?"
    elif text in ("what is your name", "whats your name", "who are you"):
        return f"I'm {BOT_NAME}, a simple rule-based chatbot."
    elif text in ("what time is it", "time"):
        return "It's " + datetime.now().strftime("%I:%M %p") + "."
    elif text == "help":
        return help_text()
    elif text in ("thanks", "thank you"):
        return "You're welcome!"
    elif text in ("bye", "goodbye"):
        return "Goodbye! Have a great day."
    else:
        return "Sorry, I don't understand that yet. Type 'help' to see what I know."


def is_goodbye(message):
    return clean(message) in ("bye", "goodbye")


def main():
    print(f"{BOT_NAME}: Hello! I'm {BOT_NAME}. Type 'bye' to exit.")
    while True:
        try:
            message = input("You: ")
        except EOFError:  # input stream ended (e.g. piped input)
            print(f"\n{BOT_NAME}: Goodbye!")
            break
        print(f"{BOT_NAME}: {get_response(message)}")
        if is_goodbye(message):
            break


if __name__ == "__main__":
    main()
