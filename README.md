# Task1-Prediction-using-Supervised-ML-Spark-Foundation

#Import Libraries:

The code begins by importing necessary libraries, including pandas for data manipulation, numpy for numerical operations, matplotlib.pyplot for plotting, seaborn for data visualization, and modules from sklearn for machine learning, such as train_test_split for data splitting and LinearRegression for building a linear regression model.

#Reading Data :

Data is read from a CSV file. This dataset likely contains two columns: 'Hours' (the number of hours studied) and 'Scores' (the corresponding percentage scores). 

#Statistics About the Dataset:

The describe() function is used to compute statistical summary information about the dataset.

#Checking Null Values:

It checks the null values in the dataset using data.isnull().sum(). This step is essential to ensure data quality.

#Data Preparation:

The data is split into two parts: the independent variable 'x' (Hours) and the dependent variable 'y' (Scores). This step prepares the data for training and testing.

#Model Training:

A linear regression model is created using LinearRegression(), and it's trained on the training data using regressor.fit(x_train, y_train).
Prediction.

#Prediction:

The model is used to predict the scores for the test data, and the predicted scores are stored in 'y_predict' with regressor.predict(x_test).


The model is used to predict the scores for the test data, and the predicted scores are stored in 'y_predict' with regressor.predict(x_test).
