# ML-Ops | Part-2, Machine Learning

This is the exercise for the second week of our ML-Ops course. This time we are working on a classification problem for which we have to create a frontend as well to make predictions with the model we trained.

# Data Exploration

We again start off with exploring our data [Link](https://www.kaggle.com/datasets/amitanshjoshi/spotify-1million-tracks/data). This time around we are working on a classification problem on about predicting a songs popularity based on certain parameters. We explore the dataset, notice imbalances and unneccesary features.

# Training

Very similar to the first week we preprocess our data by removing unwanted features, feature engineering, scaling and transforming with our pipeline. After that we use a classification estimator with a hyperparamter tuner such as GridSearchCV or RandomSearchCV. Every step we do here is being logged to mlflow again for later analysis and storing our models.

# Frontend

In this step we create a website on which we will be able to input Song-parameters and make a prediction with our model we trained wheter or not our song might be a Hit or not. This site is created using FastAPI and streamlit. 
