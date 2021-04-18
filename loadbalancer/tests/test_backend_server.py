import unittest
import pulumi
from tests import mocks

from pulumi_gcp import compute
from models import Server

test_server = Server.create_nginx_server("test-server",
    "asia-east1-a",
    "ubuntu-1804-bionic-v20210211",
    "e2-medium",
    compute.Network("network")
)

class TestingNginx(unittest.TestCase):
    # check 1: Instances have a webserver tag
    @pulumi.runtime.test
    def test_server_tags(self):
        def check_tags(args):
            actual_urn, actual_tags = args
            expected_tags = ["webserver"]
            self.assertCountEqual(actual_tags, expected_tags, f'server {actual_urn} must have webserver tag')
        return pulumi.Output.all(test_server._name, test_server.tags).apply(check_tags)
