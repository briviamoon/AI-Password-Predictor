import os
import datetime

def collect_user_interaction(input_phrase, generated_passphrase):
    """
    Records user interactions, including input phrases and generated passphrases.
    Stores the collected data in log files.

    Args:
        input_phrase (str): User's input phrase.
        generated_passphrase (str): Generated passphrase.
    """
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    log_filename = f"data_interaction_{current_date}.log"

    with open(os.path.join("logs", log_filename), "a") as logfile:
        logfile.write(f"Input phrase: {input_phrase}, Generated passphrase: {generated_passphrase}\n")

if __name__ == "__main__":
    input_phrase = input("Enter your input phrase: ")
    generated_passphrase = input("Enter the generated passphrase: ")
    collect_user_interaction(input_phrase, generated_passphrase)
