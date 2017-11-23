import virtualbox
import time


vbox = virtualbox.VirtualBox()
vm = vbox.find_machine("Win7x64")
session = virtualbox.Session()
vm.launch_vm_process(session, 'gui', '').wait_for_completion()
session = vm.create_session()
time.sleep(30)
gs = session.console.guest.create_session('User', '123')

"""Запись файла на виртуальую машину"""

gs.file_copy_to_guest("C:\\Work\\init_tests\\Repo1\\test_suite.py", "C:\\Temp\\", [])

"""Запуск теста на виртуальной машине"""

#process, stdout, stderr = gs.execute('C:\\Windows\\System32\\cmd.exe', ['cd C:\\Temp', 'python test_suite.py'])
process, stdout, stderr = gs.execute('C:\\Windows\\System32\\cmd.exe', ['/C', 'tasklist'])
#gs.close()
#session.console.power_down()