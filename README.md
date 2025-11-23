# Wine Quality Prediction

Wine quality prediction involves using machine learning algorithms to analyze and predict the quality of wine based on its chemical properties. The goal of this project is to build a model that can accurately determine wine quality using various input features.

## Project Overview

This project follows a complete machine learning workflow, including data preprocessing, model training, model serialization, and deployment using Flask.

## Workflow

### 1. Data Preprocessing
- Handled missing values
- Normalized or standardized the features
- Split the dataset into training and testing sets

### 2. Model Training
- Used a Random Forest Classifier for training
- Evaluated the model using train-test split
- Selected the model based on performance metrics

### 3. Model Serialization
- Used the pickle library to save the trained model
- Created a `model.pkl` file for prediction purposes

### 4. Flask Application
- Developed a Flask web application for real-time prediction
- Loaded the `model.pkl` file into the app
- Users can input wine chemical properties to receive a predicted quality score

## Tech Stack
- Python
- Scikit-learn
- Pandas
- NumPy
- Flask
- Pickle

## Features
- Predicts wine quality using machine learning
- End-to-end ML workflow (preprocessing → training → deployment)
- Easy-to-use Flask interface
- Fast and accurate predictions
