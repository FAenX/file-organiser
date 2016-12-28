import os
from test2 import Files
from colored import fg,bg,attr

colorpath=bg('black') + fg('white')
colorsize=bg('red') + fg('white')
reset=attr('reset')


class fileAttr(Files):

	def __init__(self,path):
		Files.__init__(self,path)
	
	def file_size(self,filepath):		
		return os.stat(filepath).st_size
	
		
		
	
	

if __name__=='__main__':
	inst=fileAttr('/media/lopus/to be deleted')
	for i in inst:
		print(colorsize +'', inst.file_size(i),'=>',colorpath + '', i + reset)
