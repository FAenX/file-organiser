#! /usr/bin/env python

import subprocess,os,sys

#clear screen
os.system('cls' if os.name=='nt' else 'clear')

def play_music():	
		try: 
			p1=subprocess.Popen('grep -i "yg" /home/lopus/new_coder/file-organiser/LISTS/FILES.LIST',shell=True,stdout=subprocess.PIPE)
			p2 = subprocess.Popen("mpv --shuffle --playlist -",shell=True,stdin=p1.stdout)
		except KeyboardInterrupt:
			sys.exit()
	
	
	
	


if __name__=='__main__':	
	play_music()
	
	
