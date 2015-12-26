import subprocess
import sys
import os
from glob import glob
import time
import filecmp



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


# create new directory on the user's desktop called "md5_verification" and inform user
# change the OUTPATH below to specify a different location for output files

outpath = os.path.expanduser("~/Desktop/md5_verification")

if not os.path.exists(outpath):
    print "Creating new metadata folder for the requested directory..."
    print ""
    os.makedirs(outpath)
# begin accumulating md5s from all .md5 files in directory and
# placing results in a single new manifest.txt file
print "Extracting pre-written md5s from md5 files..."


md5files = glob('*.md5')
md5files.sort()
countermd5 = len(md5files)
print countermd5
print md5files
for files in md5files:
	for checksum in open(files).readlines():
		print checksum
		with open(outpath + "/manifest.txt", "a+" ) as fo:
			fo.write(checksum)
	with open(outpath + "/manifest.txt", "r" ) as fo:
			filelist = fo.read()

# begin generating new md5s from all content files in directory and
# placing results in a single new nmanifest.txt file

print ""
print "Generating new md5s for payload files..."


files2analyse = glob('*.*')
files2analyse.sort()

for newsums in files2analyse:
	if not newsums.endswith('md5'):
	    
            
            
	    nchecksums = subprocess.check_output(['md5deep', '-l', newsums])
	    with open(outpath + "/nmanifest.txt", "a+" ) as fo:
			fo.write(nchecksums)
            with open(outpath + "/nmanifest.txt", "r" ) as fo:
			counterfiles = len(fo.readlines())
			
				
# compare old md5 manifest with new md5 manifest to determine any issues
print filelist
print ""
print "Comparing old md5s with new md5s..."

print counterfiles

os.chdir(outpath)
time_date = time.strftime("%Y-%m-%dT%H:%M:%S")
with open(r'nmanifest.txt', 'r') as infile,open(r'beww.txt', 'w') as outfile:
    data = infile.read()
    data = data.replace("  ", " ")
    outfile.write(data)
print data
if filecmp.cmp('manifest.txt','beww.txt' , shallow=False):
    print "YEAAAAAAH"	 
    with open("verification_result.txt", "a+" ) as fo:
    	fo.write("\nMD5 Verifier Tool\n") 
        fo.write("Date performed: %s\n" % time_date)
	fo.write("%s md5s found\n" % countermd5)
	fo.write("%s files evaluated\n" % counterfiles)
	fo.write("Result: All files are accounted for and all files match previous MD5s.\n")
	fo.write("\n")
	fo.write("Files verified:\n")
	fo.write("%s\n" % filelist)
	fo.write()
	fo.write()
	fo.write()
else:
	print "noooo"
	with open("verification_result.txt", "a+" ) as fo:
    	    fo.write("MD5 Verifier Tool\n")
            
    
            fo.write("Date performed: %s\n" % time_date)

'''    
print "$COUNTERMD5 md5s found" >> "$OUTPATH/verification_result.txt"
    print "$COUNTERFILE files evaluated" >> "$OUTPATH/verification_result.txt"
    print "Result: All files are accounted for and all files match previous MD5s." >> "$OUTPATH/verification_result.txt"
    print "" >> "$OUTPATH/verification_result.txt"
    print "Files verified:" >> "$OUTPATH/verification_result.txt"
    FILES=$(cat "$OUTPATH/manifest.txt")
    print "$FILES" >> "$OUTPATH/verification_result.txt"

RESULT=$(diff -swB manifest.txt nmanifest.txt)
'''
# determine if any problems exist based on the results of the diff function above
	    
          
'''
files2analyse = glob('*.*')
print files2aznalyse
#for newsums in files2analyse:
if not files2analyse.endswith('md5'):
            print files2analyse
	    #for nchecksums in files2analyse:
	#s	subprocess.call(['md5deep', '-l', nchecksums])
		#with open(outpath + "/nmanifest.txt", "a+" ) as fo:
		#	fo.write(checksum)
          
ls -1 | grep -v ".md5$" | while read file ; do
    md5 -r "$file"
done  | sort -k2 > "$OUTPATH/nmanifest.txt"
COUNTERFILE=$(wc -l "$OUTPATH/nmanifest.txt" | awk '{print $1}')
'''
