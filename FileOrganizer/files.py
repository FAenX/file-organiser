#! /usr/bin/env python

import os,sys
import utils

class Files(object):

	def __init__(self, target):
		self.target=target
		self.files=None
		self.init(target)
		
	def init(self,target):
		if os.path.exists(target):
			self.target=target
			self.files = (os.path.join(path,name) for path, dirs, files in os.walk(self.target) for name in files)
			return self.files				
		else:
			utils.Log.info('no files found')
			return 			 
		
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
	
		



	
	
				
			
		
	


		
		

