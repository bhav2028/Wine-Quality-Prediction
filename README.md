🍷 Wine Quality Prediction

Wine quality prediction refers to using machine learning algorithms and statistical techniques to analyze and predict the quality of wine based on various input features. The goal of this project is to develop a model that can accurately determine the quality of wine using its chemical properties.

📌 Project Overview

This project follows a complete machine learning workflow—from data preprocessing to model deployment using a Flask web application.

1️⃣ Data Preprocessing

Handled missing values

Normalized/standardized the features

Split the dataset into training and testing sets

2️⃣ Model Building

Implemented a Random Forest Classifier to train the model

Evaluated performance using the train–test split

3️⃣ Model Serialization

Used the pickle library to save the trained model

Generated a model.pkl file for future predictions

4️⃣ Web Application (Flask)

Built a simple and interactive Flask application

Integrated the model.pkl file into the app

Users can input wine chemical properties to get predicted quality

🚀 Tech Stack

Python

Scikit-learn

Pandas / NumPy

Flask

Pickle
