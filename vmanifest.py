import subprocess
import sys
import os
from glob import glob



#  Usage:  vmanifest [full path of directory]
#
#  * Assumes a single directory that contains a set of content files and a set of individual .md5 files
#  ** Generates manifest of md5s from individual md5 text files
#  ** Creates new md5s of the payload files
#  ** Runs diff against old manifest and new manifest and reports result
#  * Not recursive - input directory must contain all files directly
#
#  Remember to make the script executable: chmod +x vmanifest.sh
#
#  Requirements: for MAC OS only, assumes existence of MD5 utility that comes with MAC OS
#  This is an example script written by Bertram Lyons at IASA, 2015, in Paris, France for demonstration
#  Ported to python by Kieran O'Leary.


#  the version of the script

VERSION = 1.0


#  announce the tool
print "MD5 Manifest Verifier: Version - %s" % VERSION
print "Written for IASA  demonstration only"
print "AVPreserve, 2015; running `date`"

# syntax check (must have only one parameter: input directory)

if os.path.isdir(sys.argv[1]) == False:
	print "Syntax: %s <input directory>" % sys.argv[0]
	sys.exit()


# change to the requested directory and inform the user of such

os.chdir(sys.argv[1]) 
print ""
print "Preparing to gather md5s from the following directory as requested: "
print os.getcwd()
print ""
print ""

md5files = glob('*.md5')
md5files.sort()
print md5files
for files in md5files:
	for checksum in open(files).readlines():
		print checksum.replace("\n","")
