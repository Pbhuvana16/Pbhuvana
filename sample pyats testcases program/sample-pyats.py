from pyats import aetest
from pyats.topology import loader

testbed = loader.load('my_yaml2.yaml')

class MyTestcase(aetest.Testcase):
    @aetest.setup
    def connect_to_device(self):
        self.device= testbed.devices['sbx-ao']
        self.device.connect()

    @aetest.test
    def show_version(self):
        output = self.device.execute('show version')


        self.passed(f"Device Info:\n{output}")
 

    @aetest.cleanup
    def disconnect_from_device(self):
        self.device.disconnect()


if __name__ == '__main__':
    aetest.main()


