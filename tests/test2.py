#! /usr/bin/env python

import os,sys


class Files(object):

	def __init__(self, target, filename=None):
		self.target=target
		self._file=filename	

	def __iter__(self,ext=None):
		allfiles = (os.path.join(path,name) for path, dirs, files in os.walk(self.target) for name in files)
		if ext:			
			allfiles=(os.path.join(path,name) for path, dirs, files in os.walk(self.target) for name in files if name[name.rfind('.')+1:] is ext)
			return allfiles
					
		else:
			return allfiles
		
	def __repr__(self):
		state ='contains files from TARGET directory'
		return state
		
	def func(*args):
		pass
			
	
	
		


if __name__=='__main__':
	from colored import fg,bg,attr

	color_skip=bg('red') + fg('white')
	color_write=bg('black') + fg('white')
	reset=attr('reset')

	os.system('cls' if os.name=='nt' else 'clear')
	
	

	LOCATION = os.path.split(os.path.abspath(__file__))[0]
	ALL_FILES_LIST=None
	EXT=['.mp4','.mp3','.flv','.mkv','.3gp','.avi','.m4a','.pdf']
	directory=None
	

	if len(sys.argv) > 1:
		directory=sys.argv[1]
	
	if len(sys.argv) > 2:
		EXT=sys.argv[2:]
		if len (EXT) is 1:
			ALL_FILES_LIST=os.path.join(LIST_LOCATION,EXT[0][1:]+'.list')		
		
	if len(sys.argv) <= 1:
		print('[W]','you did not supply target')
		directory=os.path.abspath(os.getcwd())
		print('[I]','using',directory)
		
	if not os.path.exists(directory):
		print (directory,' do not exist or is not mounted')
		sys.exit()
	
	inst=Files(directory,ALL_FILES_LIST)	
	for i in inst: print(i)
	
	p=(os.path.abspath(__file__))
	d=os.path.dirname(p)
	print(d)
				
			
		
	


		
		

