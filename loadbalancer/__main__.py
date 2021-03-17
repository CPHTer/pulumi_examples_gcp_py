import pulumi
from pulumi_gcp import compute

import network_base
import servers
import load_balancer

# STEP 1. Create basic network resources
network_res = network_base.setup()

# STEP 2. Create Nginx servers
server_res = servers.setup(2, network_res["compute_network"].name)
servers_id = []
for i in range(len(server_res)):
    servers_id.append(server_res[i].id)

# STEP 3. Create load balancer
load_balancer.setup(network_res["lb_addr"].address, servers_id)

# Export properties
pulumi.export("load-balancer-ip", network_res["lb_addr"].address)
