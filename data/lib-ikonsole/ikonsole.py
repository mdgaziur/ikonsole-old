#! /usr/bin/python3.5 
# _ _  __                     _      
#(_) |/ /___  _ __  ___  ___ | | ___ 
#| | ' // _ \| '_ \/ __|/ _ \| |/ _ \
#| | . \ (_) | | | \__ \ (_) | |  __/
#|_|_|\_\___/|_| |_|___/\___/|_|\___|
#                                                                                                                                                                                                                
#  ____                _           _   _               __  __ ____  
# / ___|_ __ ___  __ _| |_ ___  __| | | |__  _   _ _  |  \/  |  _ \ 
#| |   | '__/ _ \/ _` | __/ _ \/ _` | | '_ \| | | (_) | |\/| | | | |
#| |___| | |  __/ (_| | ||  __/ (_| | | |_) | |_| |_  | |  | | |_| |
# \____|_|  \___|\__,_|\__\___|\__,_| |_.__/ \__, (_) |_|  |_|____/ 
#                                            |___/                  
#  ____           _              ____       _                           
# / ___| __ _ ___(_)_   _ _ __  |  _ \ __ _| |__  _ __ ___   __ _ _ __  
#| |  _ / _` |_  / | | | | '__| | |_) / _` | '_ \| '_ ` _ \ / _` | '_ \ 
#| |_| | (_| |/ /| | |_| | |    |  _ < (_| | | | | | | | | | (_| | | | |
# \____|\__,_/___|_|\__,_|_|    |_| \_\__,_|_| |_|_| |_| |_|\__,_|_| |_|
#                                                                       
# _   _                  
#| \ | | ___   ___  _ __ 
#|  \| |/ _ \ / _ \| '__|
#| |\  | (_) | (_) | |   
#|_| \_|\___/ \___/|_|
import getpass
import sys,os
from konsole import konsole_main
correct=False
with open('/usr/bin/lib-ikonsole/version/version.txt','r') as version_file:
	version=version_file.read()
if sys.platform == 'win32':
	print('Windows is not supported!')
	sys.exit(0)
elif sys.platform == 'darwin':
	print('MacOs is not supported!')
	sys.exit(0)
elif sys.platform == 'cygwin':
	print('It is not recommended to run ikonsole on cygwin!')
	print('Do you want to continue(Y/n)?')
	answ=input()
	if answ in 'Yy':
		pass
	else:
		sys.exit(0)
elif ('--bash' in sys.argv):
	print('Welcome to iKonsole '+version[:4]+'! Created by MD Gaziur Rahman Noor.')
	print(' _ _  __                     _      ')
	print('(_) |/ /___  _ __  ___  ___ | | ___') 
	print('| | | // _ \|  _ \/ __|/ _ \| |/ _ \ ')
	print('| | . \ (_) | | | \__ \ (_) | |  __/')
	print('|_|_|\_\___/|_| |_|___/\___/|_|\___|')
	print('Created by MD Gaziur Rahman Noor')
	print('Running in bash mode')
	print('iKonsole internal commands like "about" will not be available')
	print('Use sudo to do anything as root privilliges. Type "man sudo" for details')
	os.system('sudo bash && cd /')
elif('--n' in sys.argv) or '' in sys.argv or '--bash' in sys.argv:
	if(os.popen('id -u').read()=='0\n') or os.popen('id -u').read()=='0':
		print('Welcome to iKonsole '+version[:4]+'! Created by MD Gaziur Rahman Noor.\nRunning in Superuser Mode')
		print(' _ _  __                     _      ')
		print('(_) |/ /___  _ __  ___  ___ | | ___') 
		print('| | | // _ \|  _ \/ __|/ _ \| |/ _ \ ')
		print('| | . \ (_) | | | \__ \ (_) | |  __/')
		print('|_|_|\_\___/|_| |_|___/\___/|_|\___|')
		konsole_main(root=True)
	else:
		print('Welcome to iKonsole '+version[:4]+'! Created by MD Gaziur Rahman Noor.\nRunning in Normal Mode')
		print(' _ _  __                     _      ')
		print('(_) |/ /___  _ __  ___  ___ | | ___') 
		print('| | | // _ \|  _ \/ __|/ _ \| |/ _ \ ')
		print('| | . \ (_) | | | \__ \ (_) | |  __/')
		print('|_|_|\_\___/|_| |_|___/\___/|_|\___|')
		konsole_main()
elif('--help' in sys.argv):
	print("Usage: ikonsole [ARGUMENT]")
	print("Arguments are:")
	print("--n Starts the program in normal mode.")
	print("--help Shows this help")
	print("--h Shows this help")
	print("--bash Starts with bash")
else:
	print("Unknown command argument ",sys.argv[1:],'!')
	print("Usage: ikonsole [ARGUMENT]")
	print("Arguments are:")
	print("--n Starts the program in normal mode.")
	print("--help Shows this help")
	print("--h Shows this help")
	print("--bash Starts with bash")
