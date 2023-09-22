from pyats import aetest
from pyats.topology import loader

# 'my_yaml2.yaml' file
testbed = loader.load('my_yaml2.yaml')

class MyTestcase(aetest.Testcase):
    # Setup section runs before any test or cleanup sections
    @aetest.setup
    def connect_to_device(self):
        # Get the 'sbx-ao' device from the testbed
        self.device = testbed.devices['sbx-ao']
        
        # Connect to the device
        self.device.connect()

    @aetest.test
    def show_version(self):
        # Execute 'show version' command on the connected device
        output = self.device.execute('show version')
        
        # Print the device information
        self.passed(f"Device Info:\n{output}")

    # Cleanup section runs after all tests have completed
    @aetest.cleanup
    def disconnect_from_device(self):
        # Disconnect from the device to release resources
        self.device.disconnect()

if __name__ == '__main__':
    aetest.main()


