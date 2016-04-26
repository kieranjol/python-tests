import subprocess
import sys
import filecmp
from glob import glob
import os
import time
import csv

video_dir = sys.argv[1]
def create_csv(csv_file, *args):
    f = open(csv_file, 'wb')
    try:
        writer = csv.writer(f)
        writer.writerow(*args)
    finally:
        f.close()
        
def append_csv(csv_file, *args):
    f = open(csv_file, 'ab')
    try:
        writer = csv.writer(f)
        writer.writerow(*args)
    finally:
        f.close()
csv_filename = os.path.basename(video_dir) +  '_item_level' + time.strftime("_%Y_%m_%dT%H_%M_%S")
# CSV will be saved to your Desktop.
csvfile = os.path.expanduser("~/Desktop/%s.csv") % csv_filename       
create_csv(csvfile,('FILENAME', 'CODEC'))      
# Directory with files that we want to transcode losslessly and generate metadata for

#csv       = tkFileDialog.asksaveasfile(parent=root, defaultextension='.csv') 
for root, dirs, files in os.walk(video_dir):
    
    for filename in files:
        
        if filename.endswith(('.mov', '.mxf', '.avi', '.mp4', '.ogg', '.ogm', '.wmv','.mkv','.flv','.webm')):
             name = (os.path.join(root, filename))
             codec = subprocess.check_output(['mediainfo','--Language=raw','--Full',"--Inform=Video;%Codec%", filename]).rstrip()
             print codec
             print name
             append_csv(csvfile, (name,codec))
