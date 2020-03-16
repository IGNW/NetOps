from pyats.topology import loader
testbed = loader.load('ignwlab_dev_testbed.yaml')

# access the devices
testbed.devices

ios_1 = testbed.devices['ignw-csr']
ios_2 = testbed.devices['ignw-asav']
ios_3 = testbed.devices['ignw_nxosv']

# find links from one device to another
print("Topology Links")
for link in ios_1.find_links(ios_2):
    print("Intermachine Links to ASA: " + repr(link))
for link in ios_1.find_links(ios_3):
    print("Intermachine Links to NXOS: " + repr(link))

# establish basic connectivity
ios_1.connect()

# issue commands
print(ios_1.execute('show version'))
ios_1.configure('''
    interface GigabitEthernet2
        ip address 10.10.10.1 255.255.255.0
''')
