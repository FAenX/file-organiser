import os,sys
from optparse import OptionParser
from tings.files import Files
import testsave 

class FileOrganizer(object):

	def __init__(self):
		os.system('cls' if os.name=='nt' else 'clear')
		
		parser=OptionParser()
		parser.add_option('-t','--target',dest='target', help='target directory to be browsed')
		parser.add_option('-s','--save', help='this option creates a list with all filenamess')


		(options,args)=parser.parse_args()
		if options.target is not None:
			directory=options.target
		else:
			parser.error('you must supply target')
			sys.exit() 
		save=False	
		
		if options.save is not None:
			save=True
		
		if save:
			testsave.save(directory)
		
		else:
			testsave.show(directory)
			
		def __call__(self):
			return self.__init__()
		
		
				
if __name__=='__main__':
	FileOrganizer()
	
