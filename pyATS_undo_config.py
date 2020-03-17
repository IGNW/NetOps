from pyats.topology import loader
testbed = loader.load('ignwlab_dev_testbed.yaml')

# access the devices
testbed.devices

ios_1 = testbed.devices['ignw-csr']

# establish basic connectivity
ios_1.connect()

# issue commands
print(ios_1.execute('show version'))
ios_1.configure('''
    interface GigabitEthernet2
        no ip address
''')
