# Import libraries necessary for this project
import numpy as np
import pandas as pd
#from IPython.display import display # Allows the use of display() for DataFrames

# Import supplementary visualizations code visuals.py
#import visuals as vs

# Pretty display for notebooks
#%matplotlib inline

# Load the dataset
in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)

# Print the first few entries of the RMS Titanic data
#display(full_data.head())

def accuracy_score(truth, pred):
    """ Returns accuracy score for input truth and predictions. """

    # Ensure that the number of predictions matches number of outcomes
    if len(truth) == len(pred):

        # Calculate and return the accuracy as a percent
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)

    else:
        return "Number of predictions does not match number of outcomes!"

# Store the 'Survived' feature in a new variable and remove it from the dataset
outcomes = full_data['Survived']
data = full_data.drop('Survived', axis = 1)

def predictions_0(data):
    """ Model with no features. Always predicts a passenger did not survive. """

    predictions = []
    for _, passenger in data.iterrows():

        # Predict the survival of 'passenger'
        predictions.append(0)

    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
predictions = predictions_0(data)


def predictions_1(data):

    """ Model with one feature:
            - Predict a passenger survived if they are female. """

    predictions = []
    for _, passenger in data.iterrows():

        # Remove the 'pass' statement below
        # and write your prediction conditions here
        #pass
        if passenger['Sex'] == 'female':
            predictions.append(1)
        else:
            predictions.append(0)
#        print passenger['Sex']


    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
predictions = predictions_1(data)

def predictions_2(data):
    """ Model with two features:
            - Predict a passenger survived if they are female.
            - Predict a passenger survived if they are male and younger than 10. """

    predictions = []
    for _, passenger in data.iterrows():

        # Remove the 'pass' statement below
        # and write your prediction conditions here
        #pass
        if passenger['Sex'] == 'female':
            predictions.append(1)
        elif passenger['Sex'] == 'male' and passenger['Age'] < 10:
            predictions.append(1)
        else:
            predictions.append(0)


    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
predictions = predictions_2(data)

def predictions_3(data):
    """ Model with multiple features. Makes a prediction with an accuracy of at least 80%. """

    predictions = []
    for _, passenger in data.iterrows():

        # Remove the 'pass' statement below
        # and write your prediction conditions here
        #pass
        if passenger['Sex'] == 'female':
            if passenger["SibSp"] > 2:
                predictions.append(0)
            else:
                predictions.append(1)
        elif passenger['Sex'] == 'male' and passenger['Age'] < 10:
            predictions.append(1)
        elif passenger['Sex'] == 'male' and passenger['Age'] >= 20 and passenger['Age'] < 40 and passenger["Pclass"] == 1:
            predictions.append(1)
        elif passenger['Sex'] == 'male' and passenger["Parch"] > 1 and passenger["SibSp"] == 0 and passenger['Age'] >= 10 \
            and passenger['Age'] <=20:
            predictions.append(1)
        elif passenger['Sex'] == 'male' and passenger["Parch"] > 0 and passenger["SibSp"] == 0 and passenger['Age'] >= 10 \
            and passenger['Age'] <=20:
            predictions.append(1)
        #"Sex == 'male'", "Parch > 1", "SibSp == 1", "Pclass == 1"]
        elif passenger['Sex'] == 'male' and passenger["Parch"] > 1 and passenger["SibSp"] == 1 and passenger["Pclass"] == 1 \
            and ((passenger['Age'] >= 10 and passenger['Age'] <= 20) or (passenger['Age'] >= 30 and passenger['Age'] <= 40)):
            predictions.append(1)
        #"Sex == 'male'", "Parch == 1", "SibSp == 1", "Pclass == 1"
        elif passenger['Sex'] == 'male' and passenger["Parch"] == 1 and passenger["SibSp"] == 1 and passenger["Pclass"] == 1 \
            and passenger['Age'] >= 60:
            predictions.append(1)
        else:
            predictions.append(0)

    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
predictions = predictions_3(data)

print accuracy_score(outcomes, predictions)
