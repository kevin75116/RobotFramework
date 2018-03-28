import abc_os_manipulation
import win_vm_creator

class Win_Manipulation(abc_os_manipulation.Abc_Os_Manipulation):

    def __init__(self):
        print 'Initiate Windows manipulation object'

    def Install_Driver(self):
        print 'Install driver on Windows'
