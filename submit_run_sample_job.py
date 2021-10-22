# Import the Workspace and Datastore
from azureml.core import Workspace, Experiment, ScriptRunConfig, Environment
from azureml.core.environment import CondaDependencies



"""
Access the workspace
"""
ws = Workspace.from_config("./config")
"""
###############################################################################
"""

"""
Create virtual environment for reproductibility 
"""
myenv = Environment(name="myenv")
myenv.register(ws)
conda_dep = CondaDependencies() # create pacakges area
conda_dep.add_conda_package("scikit-learn") # add package scikit-learn
conda_dep.add_pip_package("pillow==5.4.1") # add package pillow
conda_dep.add_conda_package("pandas") # add package pandas
conda_dep.add_conda_package('azureml-sdk') # add package azureml-sdk
# put packages created into the myenv (virtualEnv)
myenv.python.conda_dependencies=conda_dep
# very important !!! set user_manager_dependecies to True !
myenv.python.user_managed_dependencies = True
# relate virtualEnv to workspace
myenv.register(ws)

"""
Create a script configuration
"""
script_config = ScriptRunConfig(source_directory=".", # current directory
                                # submit the script in the current directory
                                script="script_to_sample_job.py",
                                environment=myenv)

"""
###############################################################################
"""

"""
Create/Access an experiment object
"""
new_experiment = Experiment(
    workspace=ws,
    name="Loan-Script"
)
"""
###############################################################################
"""


"""
Submit a new run using the ScriptConfig
"""
new_run = new_experiment.submit(config=script_config)
"""
###############################################################################
"""


"""
Create a wait for completion of the script
"""
new_run.wait_for_completion()
"""
###############################################################################
"""