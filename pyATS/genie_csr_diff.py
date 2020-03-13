# Using IGNW Lab Development CSR/ASR/NXOS
# Import Genie
from genie import testbed
import pprint

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

# Determine if the Interface Protocols are the in the same state btween dev and prod
if dev_output['interfaces']['GigabitEthernet1']['protocol'] == prod_output['interfaces']['GigabitEthernet1']['protocol']:
  if dev_output['interfaces']['GigabitEthernet2']['protocol'] == prod_output['interfaces']['GigabitEthernet2']['protocol']:
    print("They have the same Interface states")
else:
  print("The Production Interfaces are in Different states")

print("Dev CSR Interfaces")
pprint.pprint(dev_output)
print("Prod CSR Interfaces")
pprint.pprint(prod_output)
