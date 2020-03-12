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
dev_output = dev_csr.parse('show interfaces description')
dev_csr.disconnect()

# Load and connect to the development CSR
prod_csr = prod_testbed.devices['ignw-csr']
prod_csr.connect()
prod_output = prod_csr.parse('show interfaces description')
prod_csr.disconnect()

# Determine if the keys are the same
if set(dev_output.keys()) == set(prod_output.keys()):
  print("They have the same Interfaces")
else:
  print("The Production Interfaces are Different"
  dev_interface_set = set(dev_output.keys())
  prod_interface_set = set(prod_output.keys())
  print("Dev has these different interfaces: "
  print(dev_interface_set.difference(prod_interface_set))
  print("Prod has these different interfaces: "
  print(prod_interface_set.difference(dev_interface_set))

# Print it nicely
import pprint
print("Dev CSR Interfaces")
pprint.pprint(dev_output)
print("Prod CSR Interfaces")
pprint.pprint(prod_output)
