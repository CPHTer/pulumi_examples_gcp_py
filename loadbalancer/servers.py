import pulumi
from pulumi_gcp import compute
from models import Server

def setup(count, compute_network):
    """Create Nginx servers.
    Args:
        count (int): The number of servers to create.
        vpc (str): In which vpc network.
    Returns:
        applied_instances (array): The applied compute instances.
    """
    applied_instances = []

    for i in range(count):
        compute_instance = Server.create_nginx_server(f"nginx-server-{i+1}",
            "asia-east1-a",
            "ubuntu-1804-bionic-v20210211",
            "e2-medium",
            compute_network
        )
        applied_instances.append(compute_instance)

    return applied_instances
