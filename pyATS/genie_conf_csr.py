# Change GigabitEthernet2 Port so we can Diff the changes
# Import Genie Conf Library
from genie import testbed
from genie.conf.base import Interfaces

# Create and Connect to CSR_dev
dev_testbed = testbed.load('ignwlab_dev_testbed.yaml')
dev_csr = dev_testbed.devices['ignw-csr']
dev_csr.connect()

# Create Interface
dev_csr_interface = Interface(device=dev_csr, name='GigabitEathernet2')
dev_csr_interface.ipv4 = "10.3.4.5"
dev_csr_interface.ipv4.netmask = "255.255.255.0"
dev_csr_interface.shutdown = False

# Verify Config
print(dev_csr_interface.build_config(apply=False))

# Add Y/N Logic
# if...
# To Apply= dev_csr_interface.build_config()
# To Remove= dev_csr_interface.build_unconfig()
