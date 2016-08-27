#-------------------------------------------------------------------------------
# Name:        File-Organiser
# Purpose:     To organize files according to their extensions
#
# Author:      Emmanuel Davidson <"davidsonkip@yahoo.com">
#
# Created:     27-8-2016
#-------------------------------------------------------------------------------
import os

cwd = '/home/hexxx/new_coder/'
save_directory_list_to=os.path.join(cwd + 'dir_list.txt')
save_file_list_to=os.path.join(cwd + 'file_list.txt')
write_extfiles_here=os.path.join(cwd,'test_dir')
file_list=[] 

#walk through some_directory and save the parent directories paths to save_to
def Walk(some_directory,save_to):
	opened_file=open(save_to,'w')	
	for d in os.walk(some_directory):
		pardir=d[0]
		print 'saving =========>>', pardir
		opened_file.write(pardir + '\n')
	opened_file.close() 
	print 'saved to =========>>', save_to

#look for files in _dir and save their paths to save_to
def isfile(_dir,save_to):
	opened_file=open(save_to,'a')
	os.chdir(_dir)
	print 'looking for files in ---------------->>', _dir

	walk=os.walk(os.getcwd())
	_tuple=walk.next()
	_tuple=_tuple[2]

	for f in _tuple:
		opened_file.write(os.path.abspath(f)+ '\n')
	opened_file.close()


#get a list of items from _file
def get_list(_file):
	print 'geting list from file ========>>', _file
	opened_file=open(_file,'r')
	read=opened_file.readlines()
	opened_file.close()
	return read
	print 'list called "read" returned ========>>giving list to extlook()'


#look for isfiles  and save their paths to save to
def look(_file,save_to):
	if os.path.exists(save_to):
		os.remove(save_to)
	
	dir_list=get_list(_file)
	for d in dir_list:
		d=d[:-1]		
		isfile(d,save_to)

#look for extension ext from list _list of files
#and write the file path with the extension to ext.txt
def extlook(_list,ext,location):
	print 'looking for extension ========>>', "'.",ext,"'"
	opened_file=open(os.path.join(location,ext +'.txt'),'w')
	
	for f in _list:
		f = f.strip()
		if f.endswith(ext):
			print 'Found...........................', f
			opened_file.write(os.path.abspath(f) + '\n')
	
	print 'file saved as =========>>',opened_file.name			
	opened_file.close()
def main():
		
	Walk('/home/hexxx/', save_directory_list_to)
	look(save_directory_list_to, save_file_list_to)
	file_list= get_list(save_file_list_to)
	
	#create directory if it does not exist	
	if not os.path.exists(write_extfiles_here):
		print 'creating directory',write_extfiles_here
		os.mkdir(write_extfiles_here)
		extlook(file_list,'mkv',write_extfiles_here)
	else:
		extlook(file_list,'mkv',write_extfiles_here)
		
		
if __name__=='__main__':
	main()
