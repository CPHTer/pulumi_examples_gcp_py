import pulumi
from pulumi_gcp import compute

def setup(address, servers):
    """Create load balancer.

    Args:
        address (str): The created ip address for this load balancer.
        servers (array): The id of backend servers.
    Returns:
        applied_res (dict): The information of applied resource.
    """

    applied_res = dict()

    # STEP 1. Create instance group
    webservers = compute.InstanceGroup("webservers",
        description = "Nginx servers",
        instances = servers,
        named_ports = [compute.InstanceGroupNamedPortArgs(
            name = "http",
            port = 80
        )],
        zone = "asia-east1-a"
    )

    # STEP 2. Add health check
    http_health_check = compute.HealthCheck("http-health-check",
        check_interval_sec = 10,
        http_health_check = compute.HealthCheckHttpHealthCheckArgs(
            port = 80
        ),
        timeout_sec = 5
    )

    # STEP 3. Create backend service
    backend_service = compute.BackendService("default-backend-service",
        health_checks = http_health_check.id,
        # Do not copy official sample, it will occur the following error:
        #   - [http_health_check.id]:  panic: Error reading level config: '' expected type 'string', got unconvertible type '[]interface {}', value: '[74D93920-ED26-11E3-AC10-0800200C9A66]'
        backends = [compute.BackendServiceBackendArgs(
            group = webservers.id
        )]
    )

    # STEP 4. Define URL map
    url_map = compute.URLMap("default-url-map",
        default_service = backend_service.id,
        host_rules = [compute.URLMapHostRuleArgs(
            hosts = ["*"],
            path_matcher = "allpaths",
        )],
        path_matchers = [compute.URLMapPathMatcherArgs(
            name = "allpaths",
            default_service = backend_service.id,
            path_rules =[compute.URLMapPathMatcherPathRuleArgs(
                paths = ["/*"],
                service = backend_service.id,
        )]
    )])

    # STEP 5. Create HTTP proxy
    target_http_proxy = compute.TargetHttpProxy("target-http-proxy",
        url_map = url_map.self_link
    )

    # STEP 6. Forwarding rule for External Network Load Balancing using Backend Services
    forwarding_rule = compute.GlobalForwardingRule("forwarding-rule",
        port_range = "80",
        target = target_http_proxy.self_link,
        ip_address = address
    )

    applied_res["webservers"] = webservers
    applied_res["http_health_check"] = http_health_check
    applied_res["backend_service"] = backend_service
    applied_res["url_map"] = url_map
    applied_res["target_http_proxy"] = target_http_proxy
    applied_res["forwarding_rule"] = forwarding_rule

    return applied_res
