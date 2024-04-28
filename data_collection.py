import os
import csv
import datetime

def collect_user_interaction(input_data, output_file):
    """
    Collects user interactions and stores them in a CSV file.

    Args:
        input_data (dict): Dictionary containing user interaction data.
        output_file (str): Path to the output CSV file.
    """
    fieldnames = ["timestamp", "user_id", "interaction_type", "interaction_data"]
    write_header = not os.path.exists(output_file)

    with open(output_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_id = input_data.get("user_id", "")
        interaction_type = input_data.get("interaction_type", "")
        interaction_data = input_data.get("interaction_data", "")

        writer.writerow({
            "timestamp": timestamp,
            "user_id": user_id,
            "interaction_type": interaction_type,
            "interaction_data": interaction_data
        })

if __name__ == "__main__":
    # Example usage
    input_data = {
        "user_id": "123",
        "interaction_type": "login",
        "interaction_data": "username: example_user"
    }
    output_file = "data/user_interactions.csv"
    collect_user_interaction(input_data, output_file)
