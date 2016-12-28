import os
from datetime import datetime



class FileAttr():
	
	def file_size(self,filepath):		
		return os.stat(filepath).st_size
		
	def last_accessed(self,filepath):
		stamp=os.stat(filepath).st_atime
		return datetime.fromtimestamp(stamp)
		
	def last_modified(self,filepath):
		stamp=os.stat(filepath).st_mtime
		return datetime.fromtimestamp(stamp)
	
	def owner(self,filepath):
		return os.stat(filepath).st_uid
	
		
		
	
	

if __name__=='__main__':
	filepath=os.path.abspath(__file__)
	inst=FileAttr()
	owner=inst.owner(filepath)
	file_size=inst.file_size(filepath)
	last_accessed=inst.last_accessed(filepath)
	last_modified=inst.last_modified(filepath)
	print(owner,file_size,last_accessed,last_modified)
	print(filepath)
	
