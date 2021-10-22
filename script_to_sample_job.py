# Import the Workspace and Datastore
from azureml.core import  Workspace, Datastore, Dataset
from azureml.core import Run
import pandas as pd

"""
Access the workspace, Datastore and Datasets
"""
ws = Workspace.from_config("./config")
az_store = Datastore.get(ws, "azure_sdk_blob1127")
az_dataset = Dataset.get_by_name(ws, "Post Verif Problem SDK")
az_default_store = ws.get_default_datastore()
"""
###############################################################################
"""

"""
Get the context 

Important !!!! 
this commande allow to submit this script insice the 170 -submit job.py
"""
new_run = Run.get_context()
"""
###############################################################################
"""

"""
Experiment will be realized as follow :

"""
#df = az_dataset.to_pandas_dataframe()
df = pd.read_csv("Loan+Approval+Prediction.csv")

df = df[["Education","Self_Employed","ApplicantIncome","CoapplicantIncome"]]

print("df is as follow : ")
print(df.head())
df.to_csv("./outputs/loan_trunc.csv", sep=";", index='False')


# log the number of observation to workspace as metrics
new_run.log("Total observation", len(df))
# log the missig data values to workspace as metrics
df_null = df.isnull().sum()
for col in df.columns:
    new_run.log(col, df_null[col])
"""
###############################################################################
"""


"""
complete en experiment run
"""
new_run.complete()
"""
###############################################################################
"""