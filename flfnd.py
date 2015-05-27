#!/usr/bin/python
#flfnd Copyright Vojtech Horanek 2015
#flfnd = FiLe FiND

import os.path
import sys
from subprocess import call

if len(sys.argv)<2:
   print"You need to specify file to be find!" 
   sys.exit()	
if (os.path.isfile(sys.argv[1])):
	print "File <%s> was found!" % sys.argv[1]
	sys.exit()
elif (sys.argv[1] == "--help"):
	print "Add (only)one file argument to command"
	print "--help                   print this screen"
	print "--autor                  autor name and email adress"
	print "--about                  about this program"
	print "-c <filename>            create new file (based on touch command)"
	sys.exit()
elif (sys.argv[1] == "--about"):
	print"Program to identify if the file exists"
	print"Copyright Vojtech Horanek 2015"
	sys.exit()
elif (sys.argv[1] == "--autor"):
	print"Vojtech Horanek <vojtechhoranek@gmail.com>"
	sys.exit()
elif (sys.argv[1] == "-c"):

	if len(sys.argv)<3:
   		print"You need to specify file name to be created!" 
   		sys.exit()
   	else:	
		call("touch " + sys.argv[2], shell=True)
		print "File %s was successfully created!" % sys.argv[2]
		sys.exit()
else:
	print"File <%s> wasn't found!" % sys.argv[1]
	print"If you want to create use <flfnd -c %s>" % sys.argv[1]
	sys.exit()
