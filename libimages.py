import sys
import subprocess
from glob import glob
import os

video_dir = sys.argv[1]
inmagic_xmlfile = 'blablabla.xml'
wd = os.path.dirname(video_dir)
os.chdir(wd)

# Find all video files to transcode
video_files =  glob('*.tif') + glob('*.jpg')
num_of_files = len (video_files)
no_of_emptyfields = num_of_files - 1
number = 0
#print noofemptyfields
with open(inmagic_xmlfile, "w+") as fo:

	fo.write('<?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?>\n')
	fo.write('<inm:Results xmlns:inm="http://www.inmagic.com/webpublisher/query" productTitle="Inmagic DB/TextWorks for SQL" productVersion="13.00">\n')
	fo.write('<inm:Recordset setCount="%s">\n' % no_of_emptyfields)
	fo.write('<inm:Record setEntry="%s">\n' % number)
	fo.write('<inm:Reference-Number/>\n')
	fo.write('<inm:Type/>\n')
	fo.write('<inm:Item-Title/>\n')
	fo.write('<inm:Film-Title/>\n')
	fo.write('<inm:Year/>\n')
	fo.write('<inm:Country-of-Origin/>\n')
	fo.write('<inm:Language/>\n')
	fo.write('<inm:Notes/>\n')
	fo.write('<inm:Dimensions/>\n')
	fo.write('<inm:Colour/>\n')
	fo.write('<inm:Location-Number/>\n')
	fo.write('<inm:Conservation/>\n')
	fo.write('<inm:Copyright/>\n')
	fo.write('<inm:Access-Restrictions/>\n')
	fo.write('<inm:Acquisition-Source/>\n')
	fo.write('<inm:Acquisition-Method/>\n')
	fo.write('<inm:Date-Created/>\n')
	fo.write('<inm:Edited-By/>\n')
	fo.write('<inm:Date-Last-Modified/>\n')
	fo.write('<inm:Number-Of-Copies/>\n')
	fo.write('<inm:Description/>\n')
	fo.write('<inm:Subject-Headings/>\n')
	fo.write('<inm:Date-Of-Donation/>\n')
	fo.write('<inm:Accession-Number/>\n')
	fo.write('<inm:Director/>\n')
	fo.write('<inm:Image/>\n')
	fo.write('<inm:Collection-Name/>\n')
	fo.write('<inm:Collection-Level-Des/>\n')
	fo.write('<inm:Level-of-Description/>\n')
	fo.write('<inm:Digital-or-Hardcopy/>\n')
	fo.write('<inm:Master-or-Access/>\n')
	fo.write('<inm:Size/>\n')
	fo.write('<inm:Digital-Size/>\n')
	fo.write('<inm:File-Format/>\n')
	fo.write('<inm:Resolution/>\n')
	fo.write('<inm:Depositor-Ref-Number/>\n')
	fo.write('<inm:Movement-Field/>\n')
	fo.write('</inm:Record>\n')
for _ in range(no_of_emptyfields):
	number += 1
	with open(inmagic_xmlfile, "a+") as fo:

		
		
			fo.write('<inm:Record setEntry="%s">\n' % number)
			fo.write('<inm:Reference-Number/>\n')
			fo.write('<inm:Type/>\n')
			fo.write('<inm:Item-Title/>\n')
			fo.write('<inm:Film-Title/>\n')
			fo.write('<inm:Year/>\n')
			fo.write('<inm:Country-of-Origin/>\n')
			fo.write('<inm:Language/>\n')
			fo.write('<inm:Notes/>\n')
			fo.write('<inm:Dimensions/>\n')
			fo.write('<inm:Colour/>\n')
			fo.write('<inm:Location-Number/>\n')
			fo.write('<inm:Conservation/>\n')
			fo.write('<inm:Copyright/>\n')
			fo.write('<inm:Access-Restrictions/>\n')
			fo.write('<inm:Acquisition-Source/>\n')
			fo.write('<inm:Acquisition-Method/>\n')
			fo.write('<inm:Date-Created/>\n')
			fo.write('<inm:Edited-By/>\n')
			fo.write('<inm:Date-Last-Modified/>\n')
			fo.write('<inm:Number-Of-Copies/>\n')
			fo.write('<inm:Description/>\n')
			fo.write('<inm:Subject-Headings/>\n')
			fo.write('<inm:Date-Of-Donation/>\n')
			fo.write('<inm:Accession-Number/>\n')
			fo.write('<inm:Director/>\n')
			fo.write('<inm:Image/>\n')
			fo.write('<inm:Collection-Name/>\n')
			fo.write('<inm:Collection-Level-Des/>\n')
			fo.write('<inm:Level-of-Description/>\n')
			fo.write('<inm:Digital-or-Hardcopy/>\n')
			fo.write('<inm:Master-or-Access/>\n')
			fo.write('<inm:Size/>\n')
			fo.write('<inm:Digital-Size/>\n')
			fo.write('<inm:File-Format/>\n')
			fo.write('<inm:Resolution/>\n')
			fo.write('<inm:Depositor-Ref-Number/>\n')
			fo.write('<inm:Movement-Field/>\n')
			fo.write('</inm:Record>\n')
		
with open(inmagic_xmlfile, "a+") as fo:
		fo.write('</inm:Recordset>\n')
		fo.write('</inm:Results>\n')	

for filename in video_files: #Begin a loop for all .mov and .mp4 files.

	
	msg ="User?"
	title = "Depositor?"
	choices = ["IFB", "BAI"]
	#user = choicebox(msg, title, choices)

	def add_to_inmagic(element, value, xmlfile):
	    subprocess.call(['xmlstarlet', 'ed', '--inplace', '-N', 'x=http://www.inmagic.com/webpublisher/query', '-u', element, '-v', value, xmlfile])
	add_to_inmagic('//inm:Collection-Name', 'BAI',inmagic_xmlfile)
	add_to_inmagic('//inm:Acquisition-Source', 'Broadcasting Authority of Ireland [BAI]',inmagic_xmlfile)
	add_to_inmagic('//inm:Acquisition-Method', 'BAI Delivery',inmagic_xmlfile)

	def get_exiftool(var_type, type, filename):
	    var_type = subprocess.check_output(['exiftool', '-b',
				                 type , filename ])
	    return var_type
	megapixels =  get_exiftool('megapixels', '-Megapixels', sys.argv[1] )
	filesize =  get_exiftool('filesize', '-FileSize', sys.argv[1] )
	codec =  get_exiftool('codec', '-FileType', sys.argv[1] )
	print codec
	print megapixels
	print filesize
	add_to_inmagic('//inm:File-Format', codec,inmagic_xmlfile)
	add_to_inmagic('//inm:Digital-Size', filesize,inmagic_xmlfile)
