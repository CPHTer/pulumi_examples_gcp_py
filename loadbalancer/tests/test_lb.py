import unittest
import pulumi
from tests import mocks

import load_balancer

test_load_balancer = load_balancer.setup("1.2.3.4", ["s_1", "s_2"])

class TestingLoadBalancer(unittest.TestCase):
    # check 1: Check host rules
    @pulumi.runtime.test
    def test_urlmap_host_rules(self):
        def check_host_rules(args):
            host_rules = args[0]
            actual_rules = []
            expected_rules = [{
                "host": "*",
                "path_matcher": "allpaths"
            }]
            for rule in host_rules:
                for host in rule["hosts"]:
                    actual_rules.append({
                        "host": host,
                        "path_matcher": rule["pathMatcher"]
                    })
            self.assertCountEqual(actual_rules, expected_rules)
        return pulumi.Output.all(test_load_balancer["url_map"].host_rules).apply(check_host_rules)

    # check 2: check patch matchers
    @pulumi.runtime.test
    def test_urlmap_path_matchers(self):
        def check_path_matchers(args):
            path_matchers = args[0]
            actual_matchers = []
            expected_matchers = [{
                "name": "allpaths",
                "path": "/*",
                "service": "default-backend-service_id"
            }]
            for matcher in path_matchers:
                for rules in matcher["pathRules"]:
                    for path in rules["paths"]:
                        actual_matchers.append({
                            "name": matcher["name"],
                            "path": path,
                            "service": rules["service"]
                        })
            self.assertCountEqual(actual_matchers, expected_matchers)
        return pulumi.Output.all(test_load_balancer["url_map"].path_matchers).apply(check_path_matchers)
