import abc 
from abc import ABCMeta, abstractmethod, abstractproperty


class Abc_Os_Manipulation(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def Install_Driver(self):
        pass
