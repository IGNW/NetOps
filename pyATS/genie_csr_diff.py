# Using IGNW Lab Development CSR/ASR/NXOS
# Import Genie
from genie import testbed

# Uses specific testbed file for Develoment side gear
dev_testbed = testbed.load('ignwlab_dev_testbed.yaml')
# Uses specific testbed file for Production side gear
prod_testbed = testbed.load('ignwlab_prod_testbed.yaml')

# Load and connect to the development CSR
dev_csr = dev_testbed.devices['ignw-csr']
dev_csr.connect()
dev_output = dev_csr.parse('show interface brief')
dev_csr.disconnect()

# Load and connect to the development CSR
prod_csr = prod_testbed.devices['ignw-csr']
prod_csr.connect()
prod_output = prod_csr.parse('show interface brief')
prod_csr.disconnect()

# Print it nicely
import pprint
print(Dev CSR Interfaces")
pprint.pprint(dev_output)
print(Prod CSR Interfaces")
pprint.pprint(prod_output)
