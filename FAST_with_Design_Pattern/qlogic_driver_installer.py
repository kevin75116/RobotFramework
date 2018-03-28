import vendor_driver_installer

class Qlogic_Driver_Installer(vendor_driver_installer.Vendor_Driver_Installer):

    def __init__(self, os_manipulation):
        self.os_manipulation = os_manipulation
        print 'Initiate Qlogic driver installer'

    def Install_Driver(self):
        self.os_manipulation.Install_Driver()
    
