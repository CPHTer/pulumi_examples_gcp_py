import pulumi

class RuntimeMocks(pulumi.runtime.Mocks):
    def new_resource(self, type_, name, inputs, provider, id_):
        # For the UT of firewall to verify LB address is in whitelist or not
        if name == "load-balancer-address":
            address = {
                "address": "1.2.3.4"
            }
            return [name + '_id', dict(inputs, **address)]
        else:
            return [name + '_id', inputs]
    def call(self, token, args, provider):
        return {}

pulumi.runtime.set_mocks(RuntimeMocks())