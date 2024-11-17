# Donald Larson
# CIS256 Fall 2024
# Programming 7 (PA7)
'''
This program demonstrates techniques for cleaning datasets using the Pandas
package.  This includes removing duplicate rows and dealing with missing
values.
'''

import pandas as pd

# Load the data set
datafile = "office_data.csv"
df = pd.read_csv(datafile)

# Print the dataset as read from the file
print("Data Before Cleaning:")
print(df)

# Remove duplicate rows.  Assume that 'ID' can be ignored.
df.drop_duplicates(subset=['Name', 'Age', 'Salary', 'Department'],
                   keep='first', inplace=True)

# Replace Nan Age values with the median value.
median_age = df['Age'].median()
print("median Age = ", median_age)
df['Age'] = df['Age'].fillna(median_age)

# Replace Nan Salary values with the mean value.
mean_salary = df["Salary"].mean()
print("mean Salary = ", mean_salary)
df['Salary'] = df['Salary'].fillna(mean_salary)

# Print the cleaned dataset
print("Cleaned Data:")
print(df)
