import re



def main():
	line='hello world.flv'	
	match=re.compile("\\..*$")
	
	if match.search(line):
		print 'True'
		return True
	else:
		print 'False'
		return False
	
		
if __name__=='__main__':
	main()
