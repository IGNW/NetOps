# Using IGNW Lab Development CSR/ASR/NXOS
# Import Genie
from genie import topology

# Uses specific testbed file for Develoment side gear
testbed = topology.load('ignwlab_dev_testbed.yaml')

# Find the device I want to connect to
csr = testbed.devices['ignw-csr']

# Connect to it
csr.connect()

# Parse device output
output = csr.parse('show version')

# Print it nicely
import pprint
pprint.pprint(output)
