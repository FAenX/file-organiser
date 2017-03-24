import os
from datetime import datetime



class FileAttr():
	
	@staticmethod
	def file_size(self,filepath):		
		return os.stat(filepath).st_size
	
	@abstractmethod
	def last_accessed(self,filepath):
		stamp=os.stat(filepath).st_atime
		return datetime.fromtimestamp(stamp)
	@staticmethod
	def last_modified(self,filepath):
		stamp=os.stat(filepath).st_mtime
		return datetime.fromtimestamp(stamp)
	
	@staticmethod
	def owner(self,filepath):
		return os.stat(filepath).st_uid
	
	@staticmethod
	def issize(self,size,filepath):
		if size == file_size(filepath):
			return True
		else:
			return False
	
	@staticmethod
	def isnotused(self,time,filepath):
		if time > last_accessed(filepath):
			return True
		else:
			return False 
			
	@staticmethod
	def isuser(self,user):
		if user == os.getuid():
			return True
		else:
			return False
		
	
	

