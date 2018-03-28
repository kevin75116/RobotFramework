import vendor_driver_installer

class Driver_Installer(object):

    def __init__(self, vendor_driver_installer):
        self.driver_installer = vendor_driver_installer

    def install_driver(self):
        self.driver_installer.Install_Driver()
