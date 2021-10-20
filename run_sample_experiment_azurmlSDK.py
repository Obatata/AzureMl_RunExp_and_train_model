# Import the Workspace and Datastore
from azureml.core import  Workspace, Datastore, Dataset, Experiment


"""
Access the workspace, Datastore and Datasets
"""
ws = Workspace.from_config("./config")
az_store = Datastore.get(ws, "azure_sdk_blob1127")
az_dataset = Dataset.get_by_name(ws, "Post Verif Problem SDK")
az_default_store = ws.get_default_datastore()



"""
Create/Access an experiment object 
"""
experiment = Experiment(
                        workspace=ws,
                        name="Loan-SDK-Exp01"
                       )

"""
########################################################################################################################
"""

"""
Run an experiment using 
"""
# start an experiement run
new_run = experiment.start_logging() # ==> start runing on azurml experiment

"""
Experiment will be realized here between start and complete !

"""
df = az_dataset.to_pandas_dataframe()

print("df is as follow : ")
print(df.head())



# log the number of observation to workspace as metrics
new_run.log("Total observation", len(df))
# log the missig data values to workspace as metrics
df_null = df.isnull().sum()
for col in df.columns:
    new_run.log(col, df_null[col])

# complete en experiment run
new_run.complete()

"""
########################################################################################################################
"""