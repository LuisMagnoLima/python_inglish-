from home_window import start_window
from message_window import message_window
from questions_window import questions_window

if __name__ == "__main__":
    start = start_window()
    if start:
        message_window()

