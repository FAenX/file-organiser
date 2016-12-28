#! /usr/bin/env python

from fileAttr import FileAttr

class Utils(object):
	
	inst=FileAttr()	
		
	def isuser(self,user):
		if user == os.getuid():
			return True
		else:
			return False
			
	def issize(self,size,filepth):
		if size == Utils.inst.file_size(filepath):
			return True
		else:
			return False
			
	def isnotused(self,time,filepath):
		if time > Utils.inst.last_accessed(filepath):
			return True
		else:
			return False 
	
	
	
if __name__=='__main__':
	import os,datetime
	filepath=os.path.abspath(__file__)
	inst=Utils()
	
	print(inst.isuser(1000))
	print(inst.issize(698,filepath))
	print(inst.isnotused(datetime.datetime.today(),filepath))
	print(Utils.inst.file_size(filepath))	
