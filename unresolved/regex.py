import re
import os

here=os.path.split(os.path.abspath(__file__))[0]
print(here)

def main():
	line='hello world.flv'	
	match=re.compile("\\..*$")
	
	if match.search(line):
		print('True')
		return True
	else:
		print ('False')	
		return False
	
		
if __name__=='__main__':
	main()
