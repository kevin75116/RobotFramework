import vendor_driver_installer

class Mlnx_Driver_Installer(vendor_driver_installer.Vendor_Driver_Installer):

    def __init__(self, os_manipulation):
        self.os_manipulation = os_manipulation
        print 'Initiate Mlnx driver installer'

    def Install_Driver(self):
        self.__preprocess()
        self.os_manipulation.Install_Driver()
    
    def __preprocess(self):
        print 'Pre-processing for drivers'
