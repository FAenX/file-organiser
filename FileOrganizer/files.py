#! /usr/bin/env python

import os,sys

class Files(object):

	def __init__(self, target=None,files=None):
		self.target=target
		self.files=files
		
	def __call__(self,target):
		if os.path.exists(target):
			self.target=target
			self.files = (os.path.join(path,name) for path, dirs, files in os.walk(self.target) for name in files)
			return self.files				
		else:
			return None 
	def __iter__(self):				
		return self.files		 
		
	def __len__(self):
		return len([a for a in self.files])
		
	def __contains__(self,*args):
		next=self.__iter__()
		while True:
			try:
				if args is next.__next__():
					return next.__next__()
			except StopIteration:
				pass
		return li				
					
	def __repr__(self):
		return 'container for files from %s'%self.target
	
		


if __name__=='__main__':
	from colored import fg,bg,attr

	
	color=bg('black') + fg('white')
	reset=attr('reset')

	os.system('cls' if os.name=='nt' else 'clear')
	
	
	directory=os.getcwd()
	

	
	inst=Files()
	inst(directory)	
	for i in inst: print(color+ '',i + reset)
	
	
				
			
		
	


		
		

