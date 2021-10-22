from azureml.core import Workspace
from azureml.core.compute import AmlCompute

"""
Accecc to workspace from config file 
"""
ws = Workspace.from_config(path="./config")

"""
###############################################################################
"""


"""
Create Computer cluster
"""
# Specify the cluster name
cluster_name = "my-cluster-1807"

# Provisionning configuration using Amlcompute
compute_config = AmlCompute.provisioning_configuration(
                                                        vm_size="STANDARD_D11_V2",
                                                        max_nodes=2
                                                      )

# Create the cluster
cluster = AmlCompute.create(ws,  cluster_name, compute_config)


"""
###############################################################################
"""
