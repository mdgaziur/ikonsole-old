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
import sys,os,subprocess
import gnureadline
with open('/usr/bin/lib-ikonsole/version/version.txt','r') as version_file:
	version=version_file.read()
try:
	from PIL import Image
	installed=True
except:
	print('The python module "PILLOW" not found!\nDo you want to install it?(Y/n)')
	an=input()
	if an in 'Yy':
		print('Installing PILLOW...')
		os.system('sudo apt install python-pip')
		os.system('sudo apt install python3-pip')
		os.system('sudo apt install python-pip && sudo apt python3-pip')
		os.system('sudo pip3 install pillow')
		try:
			from PIL import image
			installed = True
			os.system('clear')
		except:
			print('Failed to install the python module "pyDes"!')
			installed = False
			os.system('clear')
	else:
		print('The package PILLOW is not installed!\nThe command "logo" will not be available!')
		installed=False
		os.system('clear')
		try:
			from PIL import image
			installed = True
			os.system('clear')
		except:
			print('Failed to install the python module "pyDes"!')
			installed = False
			os.system('clear')
try:
	from pyDes import *
	installed1=True
except:
	print('The python module "PyDes" not found!\nDo you want to install it?(Y/n)')
	an=input()
	if an in 'Yy':
		print('Installing PyDes...')
		os.system('sudo apt install python-pip')
		os.system('sudo apt install python3-pip')
		os.system('sudo pip install pyDes')
		try:
			from pyDes import *
			installed1 = True
			os.system('clear')
		except:
			print('Failed to install the python module "pyDes"!')
			installed1 = False
			os.system('clear')
	else:
		print('The package PyDes is not installed!\nSo, the command "encrypt" will not be available!')
		installed1=False
		os.system('clear')
output=getpass.getuser()
plat=sys.platform
def konsole_main(root=False):
	while(1):
#		try:
#			if not root:
#			gnureadline.read_history_file('/home/'+output+'/.ikonsole-history')
#				os.remove('/home/'+output+'/.ikonsole-history')			
#			else:
#				gnureadline.read_history_file('/root/.ikonsole-history')
#				os.remove('/root/.ikonsole-history')
#		except:
#			#create a history file if it doesn't exists
#			if root:
#				history=open("/root/.ikonsole-history","w")
#				history.close()
#				gnureadline.read_history_file('/root/.ikonsole-history')
#			else:
#				history=open("/home/"+output+"/.ikonsole-history","w")
#				history.close()
#				gnureadline.read_history_file('/home/'+output+'/.ikonsole-history')
		#if not root:
			#print(output+'@'+plat+':'+os.getcwd()+'~$ '+'',end='')
			#import readline
			#readlin=output+'@'+plat+':'+os.getcwd()+'~$ '+''
			#readline.set_completer(readlin)
			#readline.get_completer_delims()
		#else:
			#print("root"+'@'+plat+':'+os.getcwd()+'~# '+'',end='')
			#import readline
			#readlin='root'+'@'+plat+':'+os.getcwd()+'~# '+''
			#readline.set_completer(readlin)
			#readline.get_completer_delims()
		try:
			if root:
				line=input('root'+'@'+plat+':'+os.getcwd()+'~# ')
				#try:
				#	os.remove('/root/.ikonsole-history')			
				#except:
				#	pass
				#history=open("/root/.ikonsole-history","w")
				#history.close()
				gnureadline.add_history(line)
				#gnureadline.write_history_file("/root/.ikonsole-history")
			else:

				line=input(output+'@'+plat+':'+os.getcwd()+'~$ ')
#				os.remove('/home/'+output+'/.ikonsole-history')			
#				except:
#					pass
				#history=open("/home/"+output+"/.ikonsole-history","w")
				#history.close()
				gnureadline.add_history(line)
				#gnureadline.write_history_file("/home/"+output+"/.ikonsole-history")
		except EOFError:
			print('exit')
			os.system('clear')
			sys.exit(0)
			pass
		
		except KeyboardInterrupt:
			print('exit')
			os.system('clear')
			sys.exit(0)
			pass
		#if(line!=''):
		#	if root:
		#		gnureadline.add_history(line)
		#		gnureadline.write_history_file('/root/.ikonsole-history')
		#	else:
		#		gnureadline.add_history(line)
		#		gnureadline.write_history_file("/home/"+output+"/.ikonsole-history")
		if(line=='help'):
			print('iKonsole '+version+'Help Sheet\nPossible commands are:')
			print('init\t\t\t\t\t\t\tResets to intial state.')
			print('cd\t\t\t\t\t\t\tChanges the current working directory')
			print('clear [OPTIONS]\t\t\t\t\t\tClears the window and does the works defined on option(s). To see the options type and enter: "clear help"')
			print('strpal [STRING] [OPTION]\t\t\t\tGets a string and tests and shows if it is palindrome or not according to option(s) given. Options are: -p, -pp, -pa')
			if installed1:
				print('encrypt [FILE/PATH TO FILE] [PINCODE] [OPTION]\t\tEncrypts a file.(MAX SIZE:70MiB). Keep in note that the pincode must be at least 8 characters. Options are "encrypt" "decrypt".')
			print('exit\t\t\t\t\t\t\tTerminates this console')
			if installed:
				print('logo\t\t\t\t\t\t\tShows the logo of this terminal.')
			print('about\t\t\t\t\t\t\tShows the informations of the developer and this app')
			print('platform\t\t\t\t\t\tShows the current platform using')
			print('cdir\t\t\t\t\t\t\tShows current working dircetory')
			print('rm [OPTION]...[FILE]...\t\t\t\t\tDeletes a file or directory') 
			print('shotwell*\t\t\t\t\t\tOpens the image viewer of ubuntu')
			print('nautilus**\t\t\t\t\t\tOpens the file manager of ubuntu')
			print('mkdir [OPTION]... DIRECTORY...\t\t\t\tMakes directory')
			print('dolphin** \t\t\t\t\t\tOpens the file manager of KDE(based on ubuntu)')
			print('normal\t\t\t\t\t\t\tReturns to normal user mode when using superuser mode.')
			print("Note: Press the enter key after terminating outer commands to get back to the terminal.\n* Command requires some extra softwares.\n** Command only available ubuntu.\n*** Command is still in developing")
		elif(line=='about'):
			print('Created by MD Gaziur Rahman Noor.\nEmail: mdgaziurrahmannoor@gmail.com\nSoftware name: iKonsole\n',version,'\nThe language that used to make this program: Python')
		elif line=='init':
			if root:
				os.system('clear')
				konsole_init(root=True)
				sys.exit(0)
			else:
				os.system('clear')
				konsole_init(root=False)
				sys.exit(0)
		elif(line=='cdir'):
			print('Current working directory is: ',os.getcwd())
		elif(line=='platform'):
			platform=sys.platform
			if(platform=='linux'):
				print('Current platform is "Linux"')
			elif(platform=='win32'):
				print('Current platform is "Windows"')
			elif(platform=='cygwin'):
				print('Current platform is "Windows/Cygwin"')
			elif(platform=='darwin'):
				print('Current platform is "Mac OS X"')
			else:
				print('Current platform is ',platform)
		elif(line=='exit'):
			sys.exit(0)
		elif 'cd' in line:
			line.split(' ')
			direct=line[3:]
			if(direct==''):
				if root:
					os.chdir('/root')
				else:
					os.chdir('/home/'+output)
			else:
				try:
					os.chdir(direct)
				except:
					print('No such file or directory named: ',direct,'')
					pass
		elif(line==''):
			pass
		#elif(line=="clear-history"):
		#	if root:
		#		gnureadline.add_history(line)
		#		os.remove('/root/.ikonsole-history')
		#	else:
		#		gnureadline.add_history(line)
		#		os.remove('/home/'+output+'/.ikonsole-history')
		elif(line=='logo'):
			if installed:
				try:
					img=Image.open("/usr/bin/lib-ikonsole/logo.jpg")
					img.show()
				except:
					print('Internal error occured!\nContinue?(Y/n)')
					while(1):
						try:
							ans=input()
						except EOFError:
							print('exit')
							os.system('clear')
							sys.exit(0)
							pass
						except KeyboardInterrupt:
							print('exit')
							os.system('clear')
							sys.exit(0)
							pass
						if ans in 'Yy':
							break
						elif ans in 'Nn':
							return 0
						else:
							print('Unknown answer!(Try again)')
			else:
				print('Sorry! The command "logo" is not available')
		elif line=='sudo -s':
			konsole_init(root=True,sudo=True)
		elif line=='normal':
			konsole_main(root=False)
		else:
			if root:
				os.system('sudo '+line)
			else:
				os.system(line)
def konsole_init(root=False,sudo=False):
	if root and not sudo:
		print('Welcome to iKonsole '+version[:4]+'! Created by MD Gaziur Rahman Noor.\nRunning in Superuser Mode')
		print(' _ _  __                     _      ')
		print('(_) |/ /___  _ __  ___  ___ | | ___') 
		print('| | | // _ \|  _ \/ __|/ _ \| |/ _ \ ')
		print('| | . \ (_) | | | \__ \ (_) | |  __/')
		print('|_|_|\_\___/|_| |_|___/\___/|_|\___|')
		konsole_main(root=True)
	elif root and sudo:
		konsole_main(root=True)
	else:
		print('Welcome to iKonsole '+version[:4]+'! Created by MD Gaziur Rahman Noor.\nRunning in Normal Mode')
		print(' _ _  __                     _      ')
		print('(_) |/ /___  _ __  ___  ___ | | ___') 
		print('| | | // _ \|  _ \/ __|/ _ \| |/ _ \ ')
		print('| | . \ (_) | | | \__ \ (_) | |  __/')
		print('|_|_|\_\___/|_| |_|___/\___/|_|\___|')
		konsole_main(root=False)
