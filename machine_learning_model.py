import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model(X, y):
    """
    Trains a machine learning model using the provided features (X) and labels (y).

    Args:
        X (array-like): Features for training.
        y (array-like): Labels for training.

    Returns:
        RandomForestClassifier: Trained machine learning model.
    """
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluates the trained machine learning model using test data.

    Args:
        model (RandomForestClassifier): Trained machine learning model.
        X_test (array-like): Features for testing.
        y_test (array-like): Labels for testing.

    Returns:
        float: Accuracy of the model on the test data.
    """
    # Predict labels for test data
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

if __name__ == "__main__":
    # Example usage
    X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Example features
    y = [0, 1, 0]  # Example labels
    model = train_model(X, y)
    accuracy = evaluate_model(model, X, y)
    print(f"Model accuracy: {accuracy}")
