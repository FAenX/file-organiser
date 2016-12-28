from optparse import OptionParser

parser=OptionParser()
parser.add_option('-t','--target',dest='target', help='target directory to be browsed')



(options,args)=parser.parse_args()

print(options.target)

print('s' in args)
