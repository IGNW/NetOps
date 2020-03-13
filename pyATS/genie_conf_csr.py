# Change GigabitEthernet2 Port so we can Diff the changes
# Import Genie Conf Library
from genie import testbed
from genie.libs.conf.interface.iosxe import Interface

# Create and Connect to CSR_dev
dev_testbed = testbed.load('ignwlab_dev_testbed.yaml')
dev_csr = dev_testbed.devices['ignw-csr']
dev_csr.connect()

# Create Interface
dev_csr_interface = Interface(device=dev_csr, name='GigabitEthernet2')
dev_csr_interface.ipv4 = "10.3.4.5"
dev_csr_interface.ipv4.netmask = "255.255.255.0"
dev_csr_interface.shutdown = False

# Verify Config
print(dev_csr_interface.build_config(apply=False))

answer = None
while answer not in ("A", "d"):
    answer = input("Apply changes or discard them? 'A' or 'd'")
    if answer == "A":
        dev_csr_interface.build_config()
        print("Config chages Applied")
    elif answer == "d":
         print("Config changes Discarded!")
    else:
    	print("Please enter 'A' or 'd'.")
