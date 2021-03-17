import pulumi
from pulumi_gcp import compute

def create_nginx_server(name, zone, image, machine_type, network):
    # Read init script
    with open('scripts/vm_startup_script.txt', 'r') as startup_script:
        data = startup_script.read()
    startup_script = data

    return compute.Instance(
        name,
        zone = zone,
        boot_disk = compute.InstanceBootDiskArgs(
            initialize_params = compute.InstanceBootDiskInitializeParamsArgs(
                image = image
            )
        ),
        machine_type = machine_type,
        network_interfaces = [compute.InstanceNetworkInterfaceArgs(
            network = network,
            access_configs = [compute.InstanceNetworkInterfaceAccessConfigArgs()],
        )],
        metadata_startup_script = startup_script,
        tags = ["webserver"]
    )
