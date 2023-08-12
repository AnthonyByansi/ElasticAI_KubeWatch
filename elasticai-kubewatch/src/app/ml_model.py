# ElasticAI KubeWatch - Machine Learning Model

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import os
from .helpers import load_config

class MachineLearningModel:
    def __init__(self, config_path="config/config.yaml"):
        self.config = load_config(config_path)
        self.data = self.load_data()

    def load_data(self):
        # Load historical performance data (replace with your data loading code)
        data = pd.read_csv(self.config["historical_data_path"])
        return data

    def train_model(self):
        features = self.data[["feature1", "feature2"]]  # Replace with actual feature columns
        target = self.data["target"]  # Replace with actual target column

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

        # Initialize and train the model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Make predictions on the test set
        y_pred = model.predict(X_test)

        # Calculate Mean Squared Error
        mse = mean_squared_error(y_test, y_pred)

        return model, mse

if __name__ == "__main__":
    model = MachineLearningModel()
    trained_model, mse = model.train_model()
    print(f"Trained model with Mean Squared Error: {mse}")
