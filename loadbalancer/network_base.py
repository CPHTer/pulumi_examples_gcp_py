"""Network Configurations"""
import pulumi
from pulumi_gcp import compute

def setup():
    """Create basic network resources.

    Returns:
        applied_res (dict): The information of applied resource.
    """
    applied_res = dict()

    # STEP 1. Create VPC network
    compute_network = compute.Network("network")

    # STEP 2. Create IP address for load balancer
    lb_addr = compute.GlobalAddress("load-balancer-address")

    # STEP 3. Create firewall rules to VPC network
    compute_firewall = compute.Firewall(
        "firewall",
        network = compute_network.name,
        allows = [compute.FirewallAllowArgs(
            protocol = "tcp",
            ports = ["80"]
        )],
        # Only allow the traffic from load balancer and health probe
        source_ranges = [lb_addr.address, "35.191.0.0/16", "130.211.0.0/22"]
    )

    applied_res["compute_network"] = compute_network
    applied_res["lb_addr"] = lb_addr
    applied_res["compute_firewall"] = compute_firewall

    return applied_res
