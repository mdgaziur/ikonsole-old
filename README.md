Thanks for using this version of ikonsole!






##WELCOME TO IKONSOLE HELPSHEET!


                                   





Please read this file before using iKonsole.






CONTENTS:

1.INSTALLATION.......

2.USER GUIDE.........

3.LICENSE............



______________________

##PART 1: INSTALLATION
______________________

This part will show you how to install ikonsole non portable version.

First extract all the files from the package tar.gz file. After that,

go to the extracted folder. You will see a file named install.py. Run it from command line. You will see a window. To install click on the install button.
When installed, run ikonsole in command line and it will check for missing dependencies and will ask install them. If you can’t run iKonsole, check if your file is corrupted. If corrupted, try to download and install it again. To uninstall iKonsole, just run the installer and click uninstall.

_____________________

##PART 2: USER GUIDE
_____________________

Using iKonsole is very easy!

iKonsole can be run with the defined commands to start or you can 

start it by typing only 'ikonsole' in the terminal window. And 
iKonsole cannot be run as root directly. So, you will have to
give option '--fr'(That needs password '1ks0138sna') or 
'--1ks0138sna' to run it as root. The defined ikonsole commands are:



--help or -h 

shows this help

--n 

runs the program in normal mode(Will be terminated if runned as root).

--bash 

runs this program with bash. Internal iKonsole commands like "about" will not be available.
iKonsole also has internal commands. They are:

init                                                   

Resets to intial state.

cd                                                      

Changes the current working directory

clear [OPTIONS]                                         

Clears the window and does the works defined on option(s). To see the options type and enter: "clear help"

strpal [STRING] [OPTION]                                

Gets a string and tests and shows if it is palindrome or not according to option(s) given. Options are: -p, -pp, -pa

encrypt [FILE/PATH TO FILE] [PINCODE] [OPTION]          

Encrypts a file.(MAX SIZE:70MiB). Keep in note that the pincode must be at least 8 characters. Options are "encrypt" "decrypt".

exit                                                    

Terminates this console.

logo                                                    

Shows the logo of this terminal.

about                                                   

Shows the informations of the developer and this app

platform                                                

Shows the current platform.

cdir                                                    

Shows current working dircetory

rm [OPTION]...[FILE]...                                 

Deletes a file or directory

shotwell*                                               

Opens the image viewer of ubuntu

nautilus**                                              

Opens the file manager of ubuntu

mkdir [OPTION]... DIRECTORY...                          

Makes directory

dolphin**                                               

Opens the file manager of KDE(based on ubuntu)

Note: Press the enter key after terminating outer commands to get back to the terminal.

###### * Command requires some extra softwares.

 ** Command only available ubuntu.

 *** Command is still in developing

So, you will need to just this things to use ikonsole.

_____________________

#PART 3: LICENSE
_____________________

iKonsole

Copyright 2019 MD Gaziur Rahman Noor <mdgaziurrahmannoor@gmail.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA.
