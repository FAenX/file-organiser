import hashlib

fhand = open('/home/lopus/new_coder/file-organiser/LISTS/FILES.LIST','r')
data = fhand.read()
fhand.close()
checksum = hashlib.md5(data).hexdigest()
