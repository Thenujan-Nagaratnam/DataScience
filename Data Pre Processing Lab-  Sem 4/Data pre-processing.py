# Data Pre-processing Lab Assignment

# **----- Import all libraries here -----**

import pandas as pd
import numpy as np

# Import the dataset into a data frame -----------------------------------
dataset = pd.read_csv('diabetes.csv')

# Code to pre-process the dataset goes here --------------------------------

# drop duplicate values ignoring the patient_ID
dataset.drop_duplicates(subset=dataset.columns.difference(['Patient_ID']) , inplace=True)

# fill missing values using using median value
dataset.fillna(dataset.median(), inplace=True)


# resolve out of range values
out_of_range = (dataset['Glucose'] <= 0) | (dataset['Glucose'] > 400)
dataset.loc[out_of_range, 'Glucose'] = dataset['Glucose'].mean()

out_of_range = (dataset['Pregncies'] < 0)
dataset.loc[out_of_range, 'Pregncies'] = np.abs(dataset['Pregncies'])

out_of_range = (dataset['BloodPressure'] <= 0) | (dataset['BloodPressure'] > 300)
dataset.loc[out_of_range, 'BloodPressure'] = dataset['BloodPressure'].mean()

out_of_range = (dataset['SkinThickness'] <= 0) | (dataset['SkinThickness'] > 100)
dataset.loc[out_of_range, 'SkinThickness'] = dataset['SkinThickness'].median()

out_of_range = (dataset['Insulin'] <= 0) | (dataset['Insulin'] > 1000)
dataset.loc[out_of_range, 'Insulin'] = dataset['Insulin'].median()

out_of_range = (dataset['BMI'] < 10) | (dataset['BMI'] > 60)
dataset.loc[out_of_range, 'BMI'] = dataset['BMI'].median()


# resolve outliars
z_scores = (dataset - dataset.mean()) / dataset.std()
abs_z_scores = np.abs(z_scores)
filtered_entries = (abs_z_scores < 3).all(axis=1)
dataset = dataset[filtered_entries]


# Write the pre-processed dataset into a csv file --------------------------------
pre_processed_dataset = dataset

student_id = "200647R.csv"

pre_processed_dataset.to_csv(student_id, index=False)
