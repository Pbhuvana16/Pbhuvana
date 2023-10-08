from pyats import aetest
from pyats.topology import loader

testbed = loader.load('my_yaml2.yaml')

class MyTestcase(aetest.Testcase):

    @aetest.setup
    def connect_to_device(self):
        self.device = testbed.devices['sbx-ao']
        self.device.connect()

    @aetest.test
    def get_device_changehostname(self):
        try:
            self.device = testbed.devices['sbx-ao']
            new_hostname = 'bhuvana'  # Change to the desired new hostname

            # Configure the new hostname
            self.device.configure('hostname ' + new_hostname)

            # Verify the new hostname
            output = self.device.execute('show running-config | include hostname')
            self.passed(f"Device Info:\n{output}")
        except Exception as e:
            self.failed(f"Failed to change device hostname: {str(e)}")

    @aetest.cleanup
    def cleanup_section(self):
        device = testbed.devices['sbx-ao']
        device.configure("hostname sbx-ao")
        device.disconnect()

if __name__ == '__main__':
    aetest.main()
