🍷 Wine Quality Prediction

Wine quality prediction refers to using machine learning algorithms and statistical techniques to analyze and predict the quality of wine based on various input features. The goal of this project is to develop a model that can accurately determine the quality of wine using its chemical properties.

📌 Project Overview

This project follows a complete machine learning workflow—from data preprocessing to model deployment using a Flask web application.

1️⃣ Data Preprocessing
1. Handled missing values
2. Normalized/standardized the features
3. Split the dataset into training and testing sets

2️⃣ Model Building
1. Implemented a Random Forest Classifier to train the model
2. Evaluated performance using the train–test split

3️⃣ Model Serialization
1. Used the pickle library to save the trained model
2. Generated a model.pkl file for future predictions

4️⃣ Web Application (Flask)
1. Built a simple and interactive Flask application
2. Integrated the model.pkl file into the app
3. Users can input wine chemical properties to get predicted quality

🚀 Tech Stack
1. Python
2. Scikit-learn
3. Pandas / NumPy
4. Flask
5. Pickle
