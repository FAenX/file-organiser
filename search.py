#-------------------------------------------------------------------------------
# Name:        File-Organiser
# Purpose:     To organize files according to their extensions
#
# Author:      Emmanuel Davidson <"davidsonkip@yahoo.com">
#
# Created:     27-8-2016
#-------------------------------------------------------------------------------

import os
from datetime import datetime
import re

search=str(raw_input('enter search criteria eg "explicit" >> '))
_str=search
location = os.path.join(os.getcwd(),'test_dir')
_file=os.path.join(location,'file_list.txt')


def main():
	opened_file=open(_file,'r')
	_list = opened_file.readlines()
	_stripedList=[]
	_files=[]
	#print _list
	match=re.compile(search,re.I)
	
	for line in _list:
		line=line.strip()
		#print line
		_stripedList.append(line)
	opened_file.close()

	
	for line in _stripedList:
		filepath=line	
		filename=os.path.split(line)
		filename=filename[1]
		filesize=float(os.path.getsize(filepath))/1000000 
		filesizeDisplay=str(filesize) + 'M'
		lastaccesed=datetime.fromtimestamp(os.path.getatime(line))
		if filesize < 500 and match.search(line):
			_files.append(filepath)
			

	
			print 'size =>>',filesizeDisplay, '	last accessed =>>',lastaccesed, '	Title =>>',filename
			print '--------------------------------------------------------------'
	return _files
		
if __name__=='__main__':
	
	main()
	
		
