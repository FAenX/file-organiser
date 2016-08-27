#-------------------------------------------------------------------------------
# Name:        File-Organiser
# Purpose:     To organize files according to their extensions
#
# Author:      Emmanuel Davidson <"davidsonkip@yahoo.com">
#
# Created:     27-8-2016
#-------------------------------------------------------------------------------





import os

cwd = '/home/hexxx/new_coder'

save_file_list_to=os.path.join(cwd + 'file_list.txt')

write_extfiles_here=os.path.join(cwd,'test_dir')

save_directory_list_to=os.path.join(cwd + 'dir_list.txt')

file_list=[] 

#walk through some_directory and save the parent directories to _file
def Walk(some_directory,_file):
	opened_file=open(_file,'w')	
	for d in os.walk(some_directory):
		pardir=d[0]
		print 'saving =========>>', pardir
		opened_file.write(pardir + '\n')
	opened_file.close() 
	print 'saved to =========>>', _file

def createFilesFile(files_from,_file):
	''' when passed a directory path it walks through the directory 
	and creates a file containing the file paths'''
	#get list of files and write them to a file
	opened_file=open(_file,'a')
	os.chdir(files_from)
	print 'looking for files in ---------------->>', files_from

	walk=os.walk(os.getcwd())
	_tuple=walk.next()
	_tuple=_tuple[2]

	for f in _tuple:
		opened_file.write(os.path.abspath(f)+ '\n')
	opened_file.close()

#look for all files 
def look(save_to,_file):
	if os.path.exists(save_to):
		os.remove(save_to)
	
	dir_list=get_list(_file)
	for d in dir_list:
		d=d[:-1]		
		createFilesFile(d,_file)

#look for extension ext from list _list of files
#and write the file with the extension to ext.txt
def extlook(_list,ext,location):
	''' looks for file extensions from a ist of file paths and 
	writes files of ssame extension to extension.text '''
	print 'looking for extension ========>>', "'.",ext,"'"
	opened_file=open(os.path.join(location,ext +'.txt'),'w')
	
	for f in _list:
		f = f.strip()
		if f.endswith(ext):
			print 'Found...........................', f
			opened_file.write(os.path.abspath(f) + '\n')
	
	print 'file saved as =========>>',opened_file.name			
	opened_file.close()






def get_list(_file):
	''' pass it a file and it returns a list object '''
	print 'geting list from file ========>>', _file
	opened_file=open(_file,'r')
	#get a list of files from recursed_list
	#note presence of newline character
	read=opened_file.readlines()
	opened_file.close()
	return read
	print 'list called "read" returned ========>>giving list to extlook()'

	
def main():
		
	Walk('/home/hexxx/', save_directory_list_to)		
	file_list= get_list(save_file_list_to)
	look(save_file_list_to,file_list)				
	extlook(file_list,'mkv',location)
	

if __name__=='__main__':
	main()
