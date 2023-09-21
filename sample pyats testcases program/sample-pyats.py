from pyats import aetest
from pyats.topology import loader

# Load the testbed file with your DevNet sandbox details
testbed = loader.load('my_yaml2.yaml')

# Define a testcase class
class MyTestcase(aetest.Testcase):
    
    # Setup method to connect to the device
    @aetest.setup
    def connect_to_device(self):
        # Access the 'sbx-ao' device from the loaded testbed
        self.device = testbed.devices['sbx-ao']
        # Connect to the device
        self.device.connect()

    # Test method to check device reachability
    @aetest.test
    def check_device_reachability(self):
        # Check if the device is connected
        if self.device.is_connected():
            self.passed(f"{self.device} is reachable.")
        else:
            self.failed(f"{self.device} is not reachable.")
    
    # Test method to get device information
    @aetest.test
    def get_device_info(self):
        # Execute a command to retrieve device information
        output = self.device.execute('show version')
        # Print the device information
        self.passed(f"Device Info:\n{output}")

    # Cleanup method to disconnect from the device
    @aetest.cleanup
    def disconnect_from_device(self):
        # Disconnect from the device
        self.device.disconnect()

# Main block to run the test
if __name__ == '__main__':
    aetest.main()
