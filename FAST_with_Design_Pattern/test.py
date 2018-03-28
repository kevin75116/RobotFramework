import win_manipulation
import qlogic_driver_installer
import mlnx_driver_installer
import driver_installer

os_manipulation = win_manipulation.Win_Manipulation()
print "************************"
qlogic_driver_installer = qlogic_driver_installer.Qlogic_Driver_Installer(os_manipulation)
driver_installer1 = driver_installer.Driver_Installer(qlogic_driver_installer)
driver_installer1.install_driver()
print "************************"
mlnx_driver_installer = mlnx_driver_installer.Mlnx_Driver_Installer(os_manipulation)
driver_installer2 = driver_installer.Driver_Installer(mlnx_driver_installer)
driver_installer2.install_driver()
