import os, sys
from tings.files import Files
				
class save:	
	ALL_FILES_LIST=os.path.join(os.path.dirname(os.path.abspath(__file__)),'FILES.LIST')
	def __init__(self,directory):
		self.directory=directory
		EXT=['.mp4','.mp3','.flv','.mkv','.3gp','.avi','.m4a','.pdf']
		
		if os.path.exists(save.ALL_FILES_LIST):
			os.remove(save.ALL_FILES_LIST)
	
			
		fileinst=Files()
		
		from colored import fg,bg,attr
		color_skip=bg('red') + fg('white')
		color_write=bg('black') + fg('white')
		reset=attr('reset')	
			
		with open(save.ALL_FILES_LIST,'a') as opened_file:

			for f in fileinst(self.directory):
				if f[f.rfind('.'):] in EXT:
					print(color_write+'[I]','writing',os.path.split(f)[1]+reset)
	
					opened_file.write(f+ '\n')
				else:print(color_skip+'[I]','skipping',os.path.split(f)[1]+reset)
				
	def __call__(self):
		return self.__init__()
		
class show:
	
	fileinst=Files()

	def __init__(self,directory):
		self.directory=directory
		
		try:
			
			for f in show.fileinst(self.directory):
					print('[I]',os.path.split(f)[1])
		except TypeError:
			print('directory does not exist')
			sys.exit()
					
	def	__call__(self):
		return self.__init__()
										
			
if __name__=='__main__':
	save()		
	
	
		
