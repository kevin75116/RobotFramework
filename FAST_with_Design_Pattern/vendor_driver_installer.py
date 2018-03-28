import abc 
from abc import ABCMeta, abstractmethod, abstractproperty


class Vendor_Driver_Installer(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def Install_Driver(self):
        pass
