#-------------------------------------------------------------------------------
# Name:        File-Organiser
# Purpose:     To organize files according to their extensions
#
# Author:      Emmanuel Davidson <"davidsonkip@yahoo.com">
#
# Created:     27-8-2016
#-------------------------------------------------------------------------------

import os
import datetime
import re
import sys

search_string=str(raw_input('enter search criteria eg "explicit" >> '))
#size = int(raw_input('enter size of file eg "500 means > 500" >> '))
location = os.path.join(os.getcwd(),'test_dir')
_file=os.path.join(location,'file_list.txt')

opened_file=open(_file,'r')
_list = opened_file.readlines()
_stripedList=[]
_files=[]

#print _list
match=re.compile(search_string,re.I)

for line in _list:
	line=line.strip()
	#print line
	_stripedList.append(line)
opened_file.close()


def search():
	

	
	for line in _stripedList:
		filepath=line	
		filename=os.path.split(line)
		filename=filename[1]
		filesize=float(os.path.getsize(filepath))/1000000 
		filesizeDisplay=str(filesize) + 'M'
		if filesize > size and match.search(line):
			_files.append(filepath)
			
			

	
			print 'size =>>',filesizeDisplay,' Title =>>',filepath
			print '--------------------------------------------------------------'
	return _files

def search_by_last_accesed():
	
	for line in _stripedList:
		filepath=line	
		filename=os.path.split(line)
		filename=filename[1]
		filesize=float(os.path.getsize(filepath))/1000000 
		filesizeDisplay=str(filesize) + 'M'
		lastaccesed=datetime.datetime.fromtimestamp(os.path.getctime(line))
		
			
			

	
	return _files



		
	
		

def main():
	#_search=search()
	#
	today=datetime.datetime.today()
	_search_by_last_accesed=search_by_last_accesed()
	for item in _search_by_last_accesed:
		for (k,v) in item.items():
			if today-v == datetime.timedelta(days=7):
				print k ,' :  ', v

	
		
if __name__=='__main__':
	
	main()
	
	
	
		
