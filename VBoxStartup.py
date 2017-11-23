import virtualbox
import time
from vboxapi import VirtualBoxManager

vbox = virtualbox.VirtualBox()
session = virtualbox.Session()
vm = vbox.find_machine('Win7x64')
vm.launch_vm_process(session, 'gui', '').wait_for_completion()

session = vm.create_session()
time.sleep(30)
gs = session.console.guest.create_session('User', '123')                                 #Создание сессии
process, stdout, stderr = gs.execute('C:\\Windows\\System32\\cmd.exe', ['/C', 'tasklist'])


print (stdout)

