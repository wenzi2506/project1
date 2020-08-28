#new ver on HEAD v1#


#!/usr/bin/python
import hashlib
import os
import sys


if len(sys.argv) < 2:
	sys.exit('Usage: %s filename' % sys.argv[0])

if not os.path.exists(sys.argv[1]):
	sys.exit('ERROR: File "%s" was not found!' % sys.argv[1])

with open(sys.argv[1], 'rb') as f:
	sha1 = hashlib.sha1()
	sha256 = hashlib.sha256()
	md5 = hashlib.md5()

	while True:
		chunk = f.read(16 * 1024)
		if not chunk:
			break
		sha1.update(chunk)
		sha256.update(chunk)
		md5.update(chunk)

	print("SHA1: %s" % sha1.hexdigest())
	print("SHA256: %s" % sha256.hexdigest())
	print("MD5: %s" % md5.hexdigest())

try:
    input("PRESS enter to terminate the program")
except:
    pass

