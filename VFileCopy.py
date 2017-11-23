
import virtualbox
import time
import vboxapi



vbox = virtualbox.VirtualBox()
session = virtualbox.Session()
vm = vbox.find_machine('Win7x64')
vm.launch_vm_process(session, 'gui', '').wait_for_completion()

session = vm.create_session()
time.sleep(10)
gs = session.console.guest.create_session('User', '123')

gs.copy_to("C:\Work\init_tests\Repo1", "C:\\tmp\notepad.exe")

gs.close()
