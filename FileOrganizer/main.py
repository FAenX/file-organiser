import os, sys
from FileOrganizer.files import Files
import utils
				
class Main(Files):
	def __init__(self,target):
		Files.__init__(self,target)
		self.target=target
		if utils.Config.save:
			self.save()
		else:
			self.show()
		
	#files=Files(target).files
	
	
	def save(self):			
		with open(utils.Config.filelist,'a') as opened_file:

			for f in self.files:
				if f[f.rfind('.'):] in utils.Config.EXT:
					utils.Log.info('writing %s' % os.path.split(f)[1])
	
					opened_file.write(f+ '\n')
				else:
					utils.Log.info('skipping %s ' % os.path.split(f)[1])
				
	
		
	

	
	def show(self):	
		
		for f in self.files:					
			utils.Log.info(f)
		
					
	
										
			
if __name__=='__main__':
	save()		
	
	
		
