import os,sys
from optparse import OptionParser
from FileOrganizer import main
from FileOrganizer import utils

class FileOrganizer(object):

	def __init__(self):
		os.system('cls' if os.name=='nt' else 'clear')
		
		parser=OptionParser()
		parser.add_option('-t','--target',dest='target', help='''target directory to be browsed
																 syntax file-organizer.py -t target''')

		(options,args)=parser.parse_args()
		if options.target is not None:
			target=options.target
		
		else:
			parser.error('try file-organizer.py -h for help')
			sys.exit() 
		
		utils.Config.check_filelist_location()  
		
				
		main.Main(target)
		
		
		
			
	def __call__(self):
		return self.__init__()
		
		
				
if __name__=='__main__':
	FileOrganizer()
	
