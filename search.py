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

def search(file_list,search_string):
	match=re.compile(search_string,re.I)	
	for line in file_list:
		filepath=line	
		filename=os.path.split(line)
		filename=filename[1]	
		if match.search(line):	
			print 'file name =>>',filename,' Title =>>',filepath
			print '--------------------------------------------------------------'

def search_by_last_modified(file_list,days):	
	for line in file_list:
		filepath=line	
		filename=os.path.split(line)
		filename=filename[1]
		mstat=os.stat(line).st_ctime		
		diff=datetime.datetime.today()-datetime.datetime.fromtimestamp(mstat)
		diff=diff.days
		if diff <=days: 
			print 'last modified =>>',datetime.datetime.fromtimestamp(mstat),' Title =>>',filepath
			print '--------------------------------------------------------------'
		

def search_by_size(file_list,size):
	for line in file_list:
		filepath=line	
		filename=os.path.split(line)
		filename=filename[1]
		filesize=float(os.path.getsize(filepath))/1000000 
		filesizeDisplay=str(filesize) + 'M'
		if filesize > size:	
			print 'size =>>',filesizeDisplay,' Title =>>',filepath
			print '--------------------------------------------------------------'
	
def main():

	search_string='mp4'
	location = os.path.join(os.getcwd(),'test_dir')
	_file=os.path.join(location,'file_list.txt')

	opened_file=open(_file,'r')
	_list = opened_file.readlines()
	main_List=[]
	for line in _list:
		line=line.strip()
	
		main_List.append(line)
	opened_file.close()
	
	#search(main_List,search_string)
	search_by_last_modified(main_List,10)

	
	
	
	
		
if __name__=='__main__':
	
	main()
	
	
	
		
