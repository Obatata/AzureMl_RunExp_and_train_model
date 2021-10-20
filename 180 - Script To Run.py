# Import the Workspace and Datastore
from azureml.core import  Workspace, Datastore, Dataset, Experiment
from azureml.core import Run

# """
# Access the workspace, Datastore and Datasets
# """
# ws = Workspace.from_config("./config")
# az_store = Datastore.get(ws, "azure_sdk_blob1127")
# az_dataset = Dataset.get_by_name(ws, "Post Verif Problem SDK")
# az_default_store = ws.get_default_datastore()
#
#
# """
# Create/Access an experiment object
# """
# experiment = Experiment(
#                         workspace=ws,
#                         name = "Loan-SDK-Exp01"
#                         )
#
print(Run.__doc__)