import sys
sys.path.append("/path/to/directory/containing/machine_learning_model.py")
from machine_learning_model import train_model, evaluate_model

# Sample features
X_train = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Example features for training
X_test = [[2, 3, 4], [5, 6, 7]]  # Example features for testing

# Sample labels
y_train = [0, 1, 0]  # Example labels for training
y_test = [0, 1]  # Example labels for testing



# Train the model
model = train_model(X_train, y_train)

# Evaluate the model
accuracy = evaluate_model(model, X_test, y_test)
print(f"Model accuracy: {accuracy}")
