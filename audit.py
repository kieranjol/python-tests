import subprocess
import sys
import filecmp
from glob import glob
import os
from Tkinter import *
import tkFileDialog
root = Tk()

# Create file-open dialog.
root.update()
# Directory with files that we want to transcode losslessly and generate metadata for
video_dir = tkFileDialog.askdirectory(parent=root)
#csv       = tkFileDialog.asksaveasfile(parent=root, defaultextension='.csv') 
for root, dirs, files in os.walk(video_dir):
    
    for filename in files:
        
        if filename.endswith(('.mov', '.mxf', '.avi', '.mp4')):
             print(os.path.join(root, filename))
