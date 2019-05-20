






########################


#####Installer Code#####


########################




import os,sys,time
os.system('mkdir /usr/bin/lib-ikonsole/')
print(os.getcwd())
def install():
	print(os.getcwd())
	try:
		os.path.isdir('data')
	except:
		print('Cannot find the data folder. Without that, installer cannot continue!')
		sys.exit(1)
	try:
		with open("data/ikonsole","r") as launcher:
			print('Copying launcher')
			os.system('cp data/ikonsole /usr/bin/')
			launcher=1
	except:
		print('Cannot find the launcher file! Without that you will not able to launch ikonsole from command line.\nDo you want to ignore the error?(Y/n)')
		launcher=0
		ans=input()
		if ans in 'Yy':
			print('Continuing...') 
			pass
		else:
			print('Installation aborted!')
			sys.exit(1)
	try:
		with open("data/lib-ikonsole/ikonsole.py","r") as pylauncher:
			print('Copying initiator')
			os.system('cp data/lib-ikonsole/ikonsole.py /usr/bin/lib-ikonsole')
			initiator=1
	except:
		print('Cannot find the initiator file! Without that ikonsole will not initiate.\nDo you want to ignore the error?(Y/n)')
		initiator=0
		ans=input()
		if ans in 'Yy':
			print('Continuing...') 
			pass
		else:
			print('Installation aborted!')
			sys.exit(1)
	try:
		with open("data/lib-ikonsole/konsole.py","r") as base:
			print('Copying base iKonsole program')
			os.system('cp data/lib-ikonsole/konsole.py /usr/bin/lib-ikonsole/')
			base=1
	except:
		print('Cannot find the base file! Without that, iKonsole main fucntions will not exist.\nDo you want to ignore the error?(Y/n)')
		base=0
		ans=input()
		if ans in 'Yy':
			print('Continuing...') 
			pass
		else:
			print('Installation aborted!')
			sys.exit(1)
	try:
		with open("data/lib-ikonsole/version/version.txt","r") as version:
			print('Copying version file')
			os.system('mkdir /usr/bin/lib-ikonsole/version/')
			os.system('cp data/lib-ikonsole/version/version.txt /usr/bin/lib-ikonsole/version/')
			version=1
	except:
		print('Cannot find the version file! Without that, there will be problem while trying to launch iKonsole.\nDo you want to ignore the error?(Y/n)')
		version=0
		ans=input()
		if ans in 'Yy':
			print('Continuing...') 
			pass
		else:
			print('Installation aborted!')
			sys.exit(1)
	try:
		with open("data/lib-ikonsole/logo.jpg","r") as l:
			print('Copying logo')
			os.system('cp data/lib-ikonsole/logo.jpg /usr/bin/lib-ikonsole/')
			lg=1
	except:
		print('Cannot find the logo file! Without that, the command "logo" will not be available.\nDo you want to ignore the error?(Y/n)')
		lg=0
		ans=input()
		if ans in 'Yy':
			print('Continuing...') 
			pass
		else:
			print('Installation aborted!')
			sys.exit(1)
	try:
		with open("data/encrypt","r") as enc:
			print('Copying included program "encrypt"')
			os.system('cp data/encrypt /usr/bin/')
			encrypt=1
	except:
		print('Cannot find the encrypt program file! Without that, the command "encrypt" will not be available.\nDo you want to ignore the error?(Y/n)')
		encrypt=0
		ans=input()
		if ans in 'Yy':
			print('Continuing...') 
			pass
		else:
			print('Installation aborted!')
			sys.exit(1)
	try:
		with open("data/strpal","r") as stra:
			print('Copying included program "strpal"')
			os.system('cp data/strpal /usr/bin/')
			strpal=1
	except:
		print('Cannot find the included program "strpal"! Without that, the program strpal will not be available.\nDo you want to ignore the error?(Y/n)')
		strpal=0
		ans=input()
		if ans in 'Yy':
			print('Continuing...') 
			pass
		else:
			print('Installation aborted!')
			sys.exit(1)
	installed=0
		#print(strpal,version,base,encrypt,initiator,lg,launcher)
	if version==1:
		installed+=1
		#print(installed)
	if base==1:
		installed+=1
		#print(installed)
	if encrypt==1:
		installed+=1
		#print(installed)
	if initiator==1:
		installed+=1
		#print(installed)
	if launcher==1:
		installed+=1
		#print(installed)
	if strpal==1:
		installed+=1
		#print(installed)
	if lg==1:
		installed+=1
	if installed==7: 
		return "Succesfully installed!" and 7
	elif installed!=7 and installed<7 and installed>0:
		return "Warning! Some package(s) could not be installed" and installed
	else:
		return "Fatal Error! Cannot install iKonsole!" and 0
