import os
import re
import sys
import datetime

if len(sys.argv) != 3:
    raise Exception ('You should give path and extension')

path = sys.argv[1]
ext = sys.argv[2]

print 'PATH=' + path
print 'EXT=' + ext

class Walker:
	def __init__ (self, path, ext):
		self.Path = path
		self.Extension = ext
	def List (self):
		result = []
		for root, dirs, files  in os.walk (self.Path):
			for filename in files:
				if filename.endswith (self.Extension):
					result.append (os.path.join (root, filename))
		return result

class FileReplacer:
	def __init__ (self, filename):
		self.FileName = filename

	def Replace (self, toFind):
		lines = []
		replacedLines = []
		
		f = open (self.FileName)
		lines = f.readlines ()
		
		now = datetime.datetime.now ()
		dateToken = str (now.year) + str (now.month) + str (now.day) + str (now.hour) + str (now.minute) + str (now.second)
		
		toReplace = (toFind + '%s"') % dateToken
		
		for line in lines:
			if (line.find (toFind) > 0):
				print 'FOUND' + line
				line = line.replace (toFind, toReplace)
				print 'REPLACED' + line
			replacedLines.append (line)
			
		f.close ()
		
		f = open (self.FileName, 'w')
		f.writelines (replacedLines)
		f.close ()
		
		return lines

names = Walker (path, ext).List ()
for name in names:
	print
	print 'Processing file : ' + name
	print
	FileReplacer (name).Replace ('.js"')
	FileReplacer (name).Replace ('.css"')
	

