import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix


# Load dataframe
df = pd.read_csv("Loan+Approval+Prediction.csv", sep=",")

# Select the columns from dataset
df = df[["Married",
         "Education",
         "Self_Employed",
         "ApplicantIncome",
         "LoanAmount",
         "Loan_Amount_Term",
         "Credit_History",
         "Loan_Status"
         ]]

# Clean Missing Data - Drop the columns with missing values
LoanPrep = df.dropna()

# Create Dummy variables - Not required in designer
LoanPrep = pd.get_dummies(LoanPrep, drop_first="True")
print("df_dummies : ")
print(LoanPrep.head())
# Create X and Y - Similar to "edit columns" in Train Module
Y = LoanPrep[["Loan_Status_Y"]]
X = LoanPrep.drop(["Loan_Status_Y"], axis=1)

# split Data X and Y into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=1234, stratify=Y)

# Build Logistic Regression model
lr = LogisticRegression()

# Fit the data to the Logistic regression object - Train Model
lr.fit(X_train, y_train)

# Predict the outcome using Test data - Score Model
y_predict = lr.predict(X_test)

# Get the probabilities score - Scored probabilites
y_prob = lr.predict_proba(X_test)[:, 1]

# Get confusion matrix and the accuracy/score
cm = confusion_matrix(y_true=y_test, y_pred=y_predict)
score = lr.score(X_test, y_test)
"""
Creat the scored dataset and upload to outputs 
"""
# reset index and set drop=True ==> old index will not add to columns
X_test = X_test.reset_index(drop=True)
y_test = y_test.reset_index(drop=True)

y_prob_df = pd.DataFrame(data=y_prob, columns=["Scored Probabilities"])
y_predict_df = pd.DataFrame(data=y_predict, columns=["Scored Label"])

scored_dataset = pd.concat([X_test, y_test, y_predict_df, y_prob_df], axis=1)


print("scored dataset : ")
print(scored_dataset.head())