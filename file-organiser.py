import os,sys
from optparse import OptionParser
from tings.files import Files
from tings import opts

class FileOrganizer(object):

	def __init__(self):
		os.system('cls' if os.name=='nt' else 'clear')
		
		parser=OptionParser()
		parser.add_option('-t','--target',dest='target', help='target directory to be browsed')

		(options,args)=parser.parse_args()
		if options.target is not None:
			directory=options.target
		else:
			parser.error('you must supply target')
			sys.exit() 
		save=False	
		
		if 's' in args:
			save=True
		
		if save:
			opts.save(directory)
		
		else:
			opts.show(directory)
			
	def __call__(self):
		return self.__init__()
		
		
				
if __name__=='__main__':
	FileOrganizer()
	
