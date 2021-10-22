from azureml.core import Workspace,  Experiment, ScriptRunConfig, Environment
from azureml.core.environment import CondaDependencies

"""
Access the workspace
"""
ws = Workspace.from_config(path="./config")
"""
###############################################################################
"""

"""
Create Virtual environment for roproductibility
"""
env_train_loan = Environment(name="env_train_loan")
# install packages
#-----------------
conda_packages = CondaDependencies()
conda_packages.add_pip_package("azureml-sdk")
conda_packages.add_pip_package("pandas")
conda_packages.add_pip_package("sklearn")
#----------------
# include package in the env_train_loan
env_train_loan.python.conda_dependencies = conda_packages
# very important !!! set user_manager_dependecies to True !
env_train_loan.python.user_managed_dependencies = True
# relate env_train to the workspace
env_train_loan.register(workspace=ws)
"""
###############################################################################
"""


"""
Create script configuration 
"""
script_config = ScriptRunConfig(
                                source_directory=".",
                                script="script_to_train_loan_job.py",
                                environment=env_train_loan
                                )
"""
###############################################################################
"""

"""
Create/Access an experiment object 
"""
new_experiment = Experiment(
                            workspace=ws,
                            name="Loan-training-script"
                           )
"""
###############################################################################
"""


"""
Create a new run using the subScriptCOnfig
"""
new_run = new_experiment.submit(config=script_config)
"""
###############################################################################
"""


"""
Create wait for completion script
"""
new_run.wait_for_completion()
"""
###############################################################################
"""