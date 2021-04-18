import unittest
import pulumi
from tests import mocks

import network_base

test_network_base = network_base.setup()

class TestingFirewall(unittest.TestCase):
    # check 1: Firewall should only allow TCP port 80
    @pulumi.runtime.test
    def test_firewall_ports(self):
        def check_ports(args):
            actual_ports = []
            expected_ports = ["tcp_80"]
            for allow in args[0]:
                for port in allow["ports"]:
                    actual_ports.append(allow["protocol"] + "_" + port)
            self.assertCountEqual(actual_ports, expected_ports)
        return pulumi.Output.all(test_network_base["compute_firewall"].allows).apply(check_ports)

    # check 2: Firewall should only accept the request from health probe and LB
    @pulumi.runtime.test
    def test_source_ranges(self):
        def check_source_ranges(args):
            actual_source_ranges = args[0]
            expected_source_ranges = ["1.2.3.4", "35.191.0.0/16", "130.211.0.0/22"]
            self.assertCountEqual(actual_source_ranges, expected_source_ranges)
        return pulumi.Output.all(test_network_base["compute_firewall"].source_ranges).apply(check_source_ranges)
