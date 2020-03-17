# Example
# -------
# IGNW Dev Lab Connectivity Check
import re    # Regex library
from pyats import aetest

# Setup class for testing topology testbed
class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def check_topology(self,
                       testbed,
                       ios1_name = 'ignw-csr',
                       ios2_name = 'ignw_nxosv'):
        ios1 = testbed.devices[ios1_name]
        ios2 = testbed.devices[ios2_name]

        # add them to testscript parameters
        self.parent.parameters.update(ios1 = ios1, ios2 = ios2)

        # get corresponding links
        links = ios1.find_links(ios2)

        assert len(links) >= 1, 'require one link between ios1 and ios2'

# Connection to testbed devices
    @aetest.subsection
    def establish_connections(self, steps, ios1, ios2):
        with steps.start('Connecting to %s' % ios1.name):
            ios1.connect()

        with steps.start('Connecting to %s' % ios2.name):
            ios2.connect()

# build a test loop to walk the devices and do the ping tests
@aetest.loop(device = ('ios1', 'ios2'))
class PingTestcase(aetest.Testcase):

    @aetest.test.loop(destination = ('10.0.0.1', '10.0.0.5'))
    def ping(self, device, destination):
        try:
            result = self.parameters[device].ping(destination, vrf='management')

        except Exception as e:
            self.failed('Ping {} from device {} failed with error: {}'.format(
                                destination,
                                device,
                                str(e),
                            ),
                        goto = ['exit'])
        else:
            print(result)
            print(self.parameters[device])
            if 'csr' in str(self.parameters[device]):
                match = re.search(r'Success rate is (?P<rate>\d+) percent', result)
                success_rate = match.group('rate')
                print('Ping {} with success rate of {}%'.format(destination, success_rate))
            elif 'nxos' in str(self.parameters[device]):
                match = re.search(r'(?P<rate>\b[0-9.]+\b)% packet loss',result)
                success_rate = match.group('rate')
                print('Ping {} with packet loss of {}%'.format(destination, success_rate))
            else:
                print('Device OS not recognized')

# post processing cleanup area
class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect(self, steps, ios1, ios2):
        with steps.start('Disconnecting from %s' % ios1.name):
            ios1.disconnect()

        with steps.start('Disconnecting from %s' % ios2.name):
            ios2.disconnect()

if __name__ == '__main__':
    import argparse
    from pyats.topology import loader

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest = 'testbed',
                        type = loader.load)

    args, unknown = parser.parse_known_args()

    aetest.main(**vars(args))
    
