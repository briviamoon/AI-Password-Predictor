import os

def collect_user_feedback(feedback_data, feedback_file):
    """
    Collects user feedback and stores it in a text file.

    Args:
        feedback_data (str): User feedback data.
        feedback_file (str): Path to the feedback text file.
    """
    with open(feedback_file, mode='a') as file:
        file.write(feedback_data + '\n')

if __name__ == "__main__":
    # Example usage
    feedback_data = "The generated passphrase is easy to remember."
    feedback_file = "user_feedback.txt"
    collect_user_feedback(feedback_data, feedback_file)
