#! /bin/bash 
# _ _  __                     _      
#(_) |/ /___  _ __  ___  ___ | | ___ 
#| | ' // _ \| '_ \/ __|/ _ \| |/ _ \
#| | . \ (_) | | | \__ \ (_) | |  __/
#|_|_|\_\___/|_| |_|___/\___/|_|\___|
#                                                                                                                                                                                                                
# _                           _                                                                                                                                                                                  
#| |    __ _ _   _ _ __   ___| |__   ___ _ __                                                                                                                                                                    
#| |   / _` | | | | '_ \ / __| '_ \ / _ \ '__|                                                                                                                                                                   
#| |__| (_| | |_| | | | | (__| | | |  __/ |                                                                                                                                                                      
#|_____\__,_|\__,_|_| |_|\___|_| |_|\___|_|
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
echo 'Launching iKonsole'
if ! hash python3 2>/dev/null; then
	echo 'Python3 is not installed! Do you want to install it?(Y/n)'
    read prompt
    testseq="Y"
    echo $prompt
    if [ $prompt = *Y* ]; then
    	echo 'Installing python3 on linux'
    	apt-get install python3
	    elif [ $prompt = *y*  ]
    	then
    		echo 'Installing python3 on linux'
    		apt-get install python3
    	elif [ $prompt = *n* ]
    	then

    		echo 'Terminating...'
    		sleep 0.900
    		exit
    	elif [ $prompt = *N* ]
    	then

    		echo 'Terminating...'
    		sleep 0.900
    		exit
    	else
    		echo 'Invalid command! Terminating...'
    		sleep 0.900
    		exit
    fi
else
    echo 'Python3 installed! Continuing'
    if [ $# -eq 0 ] ; then
    	sleep 0.900
    	clear
    	python3.5 '/usr/bin/lib-ikonsole/ikonsole.py' --n
    	exit 
    exit 0
	fi
	while [ ! $# -eq 0 ]
	do
		case "$1" in
			    --help | -h)
					echo 'Usage: ikonsole [ARGUMENT]'
					echo '--help or -h shows this help'
					echo '--n runs the program in normal mode'.
					echo '--bash runs this program with bash. Internal iKonsole commands like "about" will not be available.'
					exit
					;;
				--n)
					sleep 0.900
					clear
					python3.5 '/usr/bin/lib-ikonsole/ikonsole.py' --n
					exit
					;;
				--bash)
					sleep .900
					clear
					python3.5 '/usr/bin/lib-ikonsole/ikonsole.py' --bash
					;;
				*) 
					echo 'Unknown command'' "'$1'"!'
					echo 'Usage: ikonsole [ARGUMENT]'
					echo '--help or -h shows this help'
					echo '--n runs the program in normal mode'.
					echo '--bash runs this program with bash. Internal iKonsole commands like "about" will not be available.'
					;;
		esac
			exit
	done
fi
